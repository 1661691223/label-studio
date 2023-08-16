# Generated by Django 3.2.19 on 2023-08-10 23:04

from django.db import migrations
from django.core.paginator import Paginator
from django.db import connection

# chosen to be small enough to not cause memory issues, but large enough to not cause too many queries
# and avoid locking the entire table for too long
BATCH_SIZE = 1000

def set_project_from_task(apps, schema_editor):
    Prediction = apps.get_model('tasks', 'Prediction')

    connection.queries_log.clear()

    predictions_with_task = Prediction.objects.all().select_related('task')

    # Break the update into batches using Paginator
    paginator = Paginator(predictions_with_task, BATCH_SIZE)

    for page_num in paginator.page_range:
        page = paginator.page(page_num)
        predictions_to_update = []
        for prediction in page.object_list:
            prediction.project_id = prediction.task.project_id
            predictions_to_update.append(prediction)

        # Bulk update the current batch of predictions
        Prediction.objects.bulk_update(predictions_to_update, ['project_id'])


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('tasks', '0041_prediction_project'),
    ]

    operations = [
        migrations.RunPython(set_project_from_task, migrations.RunPython.noop),
    ]
