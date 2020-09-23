from uuid import uuid4
import datetime

from django.db import models
import humanize


def natural_datetime (dt_aware):
    dt = dt_aware.replace(tzinfo=None)
    today = datetime.date.today()

    if (today == dt.date()):
        return humanize.naturaltime(dt)

    natural_date = humanize.naturaldate(dt)
    natural_time = dt.strftime('%H:%M')
    return f'{natural_date} at {natural_time}'



class AbstractBaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class Game(AbstractBaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_game')
        ]


class Level(AbstractBaseModel):
    name = models.CharField(max_length=200)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.game} - {self.name}'

    class Meta:
        ordering = ['game', 'name']
        constraints = [
            models.UniqueConstraint(fields=['game', 'name'], name='unique_level')
        ]


class Mode(AbstractBaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_mode')
        ]


class MatchType(AbstractBaseModel):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    mode = models.ForeignKey(Mode, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.level} - {self.mode}'

    class Meta:
        ordering = ['level', 'mode']
        constraints = [
            models.UniqueConstraint(fields=['level', 'mode'], name='unique_match_type')
        ]


class Match(AbstractBaseModel):
    type = models.ForeignKey(MatchType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.type} - {natural_datetime(self.created_at)}'
