from django.db import models

class MOU(models.Model):
    CATEGORY_CHOICES = [
        ('College', 'College'),
        ('Department', 'Department'),
        ('Industry', 'Industry'),
    ]

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    sub_department = models.CharField(max_length=100, null=True)

    start_date = models.DateField()
    end_date = models.DateField()
    document = models.FileField(upload_to='mou_documents/', null=True)  # Path to store the uploaded file


    
    class Meta:
        db_table = 'mou'

    def __str__(self):
        return self.name
