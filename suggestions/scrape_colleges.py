import requests
from bs4 import BeautifulSoup
from suggestions.models import College

def scrape_college_data():
    url = 'https://www.hotcoursesabroad.com/india/us-usa/international/schools-colleges-university/211/list.html'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    colleges = []
    
    for college in soup.find_all('div', class_='college'):
        name = college.find('h2').text
        location = college.find('span', class_='location').text
        min_gpa = float(college.find('span', class_='min_gpa').text)
        min_gre_score = int(college.find('span', class_='min_gre_score').text)
        min_toefl_score = int(college.find('span', class_='min_toefl_score').text)
        min_duolingo_score = int(college.find('span', class_='min_duolingo_score').text)
        min_ielts_score = float(college.find('span', class_='min_ielts_score').text)
        
        colleges.append(College(name=name, location=location, min_gpa=min_gpa, min_gre_score=min_gre_score, min_toefl_score=min_toefl_score, min_duolingo_score=min_duolingo_score, min_ielts_score=min_ielts_score))
    
    College.objects.bulk_create(colleges)

if __name__ == '__main__':
    scrape_college_data()
