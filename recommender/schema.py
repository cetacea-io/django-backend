import graphene
import django_filters
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from courses.models import Course
from category.models import Category

from courses.schema import CourseType
from taxonomies.schema import CategoryType, TagType

class Query(graphene.ObjectType):
    recommend_courses_by_course = graphene.List(CourseType,
                                            id=graphene.Int())

    courses = graphene.List(CourseType,
                            category=graphene.Int())

    recommend_categories = graphene.List(CategoryType)

    def resolve_recommend_courses_by_course(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Course.objects.filter(published=True)[:10]
    
    def resolve_recommend_categories(self, info, **kwargs):
        return Category.objects.all()


#     def resolve_courses(self, info, **kwargs):
#         category = kwargs.get('category')

#         if category is not None:
#             return Course.objects.filter(published=True, category=category)
#         else:
#             return Course.objects.filter(published=True)


# class Recommender():
#     def recommendCourse(self, iteration):
#         if info.context.user.is_authenticated:
#             user_interests = info.context.user.profile.interests
#         best_score = 0
#         for course in Course.objects.filter(published=True):
#             match_score = 0
#             for cateogry in course.categories:
#                 if 
















# from django_pandas.io import read_frame

# import pandas as pd

# Load movies Metadata
# qs = Course.objects.filter(id=1)
# qs = Course.objects.get(id=1).values()
# print(vars(qs.categories))
# cols = ['id', 'title']
# metadata = read_frame(qs, cols)
# pd.options.display.max_columns = None
# print(metadata.head(10))
# print(metadata.columns.values)


# cats = []
# cats.append(MyClass(1, list(Category.objects.filter(courses_course_related__id=1) ) ) )
# categories = {'id': 1, 'categories': list(Category.objects.filter(courses_course_related__id=1)) }
# cols_categories = ['id', 'title']
# categories = pd.DataFrame(categories)
# print(list(for x in Category.objects.filter(courses_course_related__id=1) return x.title))
# qs_categories = Category.objects.filter(courses_course_related__id=1)
# categories = qs_categories
# categories = read_frame(qs_categories, cols_categories)
# print(list(categories))
# print(qs_categories)
# print(Category.objects.filter(courses_course_related__id=1))
# print(categories)
# keywords = pd.read_csv('../../../../the-movies-dataset/keywords.csv')

# keywords['id'] = keywords['id'].astype('int')
# categories['id'] = categories['id'].astype('int')
# metadata['id'] = metadata['id'].astype('int')

# metadata = metadata.merge(categories, on='id')
# metadata = metadata.merge(keywords, on='id')


# print(metadata)
# print(metadata.columns.values)

# def get_recommendations(id, cosine_sim):
#     idx = indices[id]
#     sim_scores = list(enumerate(cosine_sim[idx]))
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#     sim_scores = sim_scores[1:11]
#     movie_indices = [i[0] for i in sim_scores]
    # return metadata['id'].iloc[movie_indices]



# from ast import literal_eval

# features = ['categories']
# for feature in features:
#     metadata[feature] = metadata[feature].apply(literal_eval)

# import numpy as np

# def get_director(x):
#     for i in x:
#         if i['job'] == 'Director':
#             return i['name']
#     return np.nan

# def get_list(x):
#     if isinstance(x, list):
#         names = [i['name'] for i in x]
#         if len(names) > 3:
#             names = names[:3]
#         return names
#     return []

# metadata['director'] = metadata['crew'].apply(get_director)

# features = ['categories__title']
# for feature in features:
#     metadata[feature] = metadata[feature].apply(get_list)



# def clean_data(x):
#     if isinstance(x, list):
#         return [str.lower(i.replace(" ", "")) for i in x]
#     else:
#         if isinstance(x, str):
#             return str.lower(x.replace(" ", ""))
#         else:
#             return ''

# features = ['categories']

# for feature in features:
#     metadata[feature] = metadata[feature].apply(clean_data)

# def create_soup(x):
#     return ' '.join(x['categories']) + ' ' + ' '.join(x['title'])


# metadata['soup'] = metadata.apply(create_soup, axis=1)


# from sklearn.feature_extraction.text import CountVectorizer

# count = CountVectorizer(stop_words="english")

# count_matrix = count.fit_transform(metadata['soup'])

# from sklearn.metrics.pairwise import cosine_similarity

# cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

# metadata = metadata.reset_index()
# indices = pd.Series(metadata.index, index=metadata['id'])

# print(get_recommendations('1', cosine_sim2))
# print(get_recommendations('The Godfather', cosine_sim2))

















#%%
# import pandas as pd

# Load movies Metadata
# metadata = pd.read_csv('../../../../the-movies-dataset/movies_metadata.csv', low_memory=False)


# metadata.head(3)

# C = metadata['vote_average'].mean()

# m = metadata['vote_count'].quantile(0.90)

# metadata = metadata.copy().loc[metadata['vote_count'] >= m]
# metadata.shape

# def weighted_rating(x, m=m, C=C):
#     v = x['vote_count']
#     R = x['vote_average']
#     return (v/(v+m) * R) + (m/(m+v) * C)

# # q_movies['score'] = q_movies.apply(weighted_rating, axis=1)

# # print(C)




# def get_recommendations(title, cosine_sim):
#     idx = indices[title]
#     sim_scores = list(enumerate(cosine_sim[idx]))
#     sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
#     sim_scores = sim_scores[1:11]
#     movie_indices = [i[0] for i in sim_scores]
#     return metadata['title'].iloc[movie_indices]







# credits = pd.read_csv('../../../../the-movies-dataset/credits.csv')

# keywords = pd.read_csv('../../../../the-movies-dataset/keywords.csv')

# metadata = metadata.drop([19730, 29503, 35587])

# keywords['id'] = keywords['id'].astype('int')
# credits['id'] = credits['id'].astype('int')
# metadata['id'] = metadata['id'].astype('int')

# metadata = metadata.merge(credits, on='id')
# metadata = metadata.merge(keywords, on='id')

# print(metadata.head(10))

# from ast import literal_eval

# features = ['cast', 'crew', 'keywords', 'genres']
# for feature in features:
#     metadata[feature] = metadata[feature].apply(literal_eval)

# import numpy as np

# def get_director(x):
#     for i in x:
#         if i['job'] == 'Director':
#             return i['name']
#     return np.nan

# def get_list(x):
#     if isinstance(x, list):
#         names = [i['name'] for i in x]
#         if len(names) > 3:
#             names = names[:3]
#         return names
#     return []

# metadata['director'] = metadata['crew'].apply(get_director)

# features = ['cast', 'keywords', 'genres']
# for feature in features:
#     metadata[feature] = metadata[feature].apply(get_list)



# def clean_data(x):
#     if isinstance(x, list):
#         return [str.lower(i.replace(" ", "")) for i in x]
#     else:
#         if isinstance(x, str):
#             return str.lower(x.replace(" ", ""))
#         else:
#             return ''

# features = ['cast', 'keywords', 'director', 'genres']

# for feature in features:
#     metadata[feature] = metadata[feature].apply(clean_data)

# def create_soup(x):
#     return ' '.join(x['keywords']) + ' ' + ' '.join(x['cast']) + ' ' + x['director'] + ' ' + ' '.join(x['genres'])


# metadata['soup'] = metadata.apply(create_soup, axis=1)


# from sklearn.feature_extraction.text import CountVectorizer

# count = CountVectorizer(stop_words="english")

# count_matrix = count.fit_transform(metadata['soup'])

# from sklearn.metrics.pairwise import cosine_similarity

# cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

# metadata = metadata.reset_index()
# indices = pd.Series(metadata.index, index=metadata['title'])

# print(get_recommendations('The Dark Knight Rises', cosine_sim2))
# print(get_recommendations('The Godfather', cosine_sim2))
