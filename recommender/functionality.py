from courses.models import Course

def recommend_courses_by_course(total):
    # if id is not None:
    return Course.objects.filter(published=True)[:total]