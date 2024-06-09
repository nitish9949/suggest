import pandas as pd
from django.core.management.base import BaseCommand
from suggestions.models import College

class Command(BaseCommand):
    help = 'Load college data from an Excel file into the database'

    def handle(self, *args, **kwargs):
        # Specify the path to your Excel file
        excel_file_path = 'C:/Users/nitis/Desktop/uni1.xlsx'  # Using raw string
        
        # Read the Excel file into a DataFrame using openpyxl engine
        df = pd.read_excel(excel_file_path, engine='openpyxl')
        
        # Iterate through the DataFrame and create College instances
        for _, row in df.iterrows():
            college = College(
                name=row['University Name'],
                min_gpa=row['Minimum GPA (10-scale)'],
                min_gre_score=row['GRE Score'],
                min_toefl_score=row['TOEFL Score'],
                min_duolingo_score=row['Duolingo Score'],
                min_ielts_score=row['IELTS Score']
            )
            college.save()

        self.stdout.write(self.style.SUCCESS('Successfully loaded college data from Excel file'))
