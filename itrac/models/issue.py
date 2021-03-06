from django.conf import settings
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _
from markdown import markdown

from ..itrac_utils import unique_slug_generator
from .project import Project
from .tag import Tag

#from django.apps import apps
#MyModel1 = apps.get_model('app1', 'MyModel1')

class ISSUE_TYPE(models.TextChoices):
    BREAK_FIX =     '01', _('Break/fix')
    FEATURE =       '02', _('New feature')
    OPTIMIZATION =  '03', _('Optimization')
    TASK =          '04', _('Task')


class ISSUE_STATUS(models.TextChoices):
    OPEN =              '01', _('Open')
    INVESTIGATE =       '02', _('Investigate')
    TRIAGE =            '03', _('Await Approval')

    BUILD_IN_PROGRESS = '10', _('Build in DEV')
    VALIDATING_DEV =    '11', _('Validating in DEV')
    READY_FOR_STAGE =   '19', _('Ready for STAGING')

    BUILD_IN_STAGE =    '20', _('Build in STAGING')
    VALIDATING_STAGE =  '21', _('Validating in STAGING')
    READY_FOR_PROD =    '29', _('Ready for PROD')

    BUILD_IN_PROD =     '30', _('Build in PROD')
    VALIDATING_PROD =   '31', _('Validating in PROD')
    VALIDATED_PROD =    '32', _('Validated in PROD')

    COMPLETE =          '80', _('Complete')
    CLOSED =            '90', _('Closed')


class ISSUE_PRIORITY(models.TextChoices):
    PRIORITY_1 =  '1', _('1 - highest')
    PRIORITY_2 =  '2', _('2')
    PRIORITY_3 =  '3', _('3')
    PRIORITY_4 =  '4', _('4')
    PRIORITY_5 =  '5', _('5 - lowest')

class Issue(models.Model):
    """
    A single Issue
    """
    # This id is generated by the post_save signal
    # coded_id = project.code + Issue.pk
    coded_id = models.CharField(max_length=40, null=True)

    project = models.ForeignKey(Project, related_name='issues', null=True, on_delete=models.CASCADE)
    issue_type = models.CharField(max_length=2, choices=ISSUE_TYPE.choices, default=ISSUE_TYPE.BREAK_FIX)
    status = models.CharField(max_length=2, choices=ISSUE_STATUS.choices, default=ISSUE_STATUS.OPEN)
    priority = models.CharField(max_length=1, choices=ISSUE_PRIORITY.choices, null=True)

    title = models.CharField(max_length=200)
    description = models.TextField(max_length=4000, blank=True)
    slug = models.CharField(max_length=250, blank=True)

    is_resolved = models.BooleanField(default=False)
    resolved_date = models.DateField(blank=True, null=True)
    resolution_details = models.CharField(max_length=250, blank=True, null=True)

    upvotes = models.IntegerField('likes', default=0)

    tags = models.ManyToManyField(Tag, related_name='issues', blank=True)

    # image = models.ImageField(upload_to='img', blank=True, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
            settings.AUTH_USER_MODEL,
            related_name='+',
            on_delete=models.CASCADE, blank=True
        )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        on_delete=models.CASCADE
    )
    assignee = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='+',
        null=True,
        on_delete=models.CASCADE
    )

    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    class Meta:
        verbose_name = "issue"
        verbose_name_plural = "issues"
        ordering = ['title']
        indexes = [
            models.Index(fields=['title',]),
            models.Index(fields=['coded_id',]),
        ]

    def __str__(self):
        return f'{self.coded_id} {self.title}'

    # @property
    # def issue_id(self):
    #     return f"{self.project.code}-{self.id}"

    def get_absolute_url(self):
        return reverse('itrac:issue_detail', args=(self.pk,))

    def get_description_as_markdown(self):
        return mark_safe(markdown(self.description, safe_mode='escape'))

    @property
    def get_watchers(self):
        names = [ w.full_name for w in self.watchers.all()]
        return ', '.join(names)


# update the issue.coded_id
@receiver(post_save, sender=Issue)
def set_issue_coded_id(sender, instance, created, **kwargs):
    if created:
        instance.coded_id = f'{ instance.project.code }-{ instance.pk }'
        instance.save()

# update the issue_prefix
@receiver(pre_save, sender=Issue)
def set_issue_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
