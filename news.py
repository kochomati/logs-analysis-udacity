#! /usr/bin/env python

import psycopg2
DBNAME = "news"

#1. What are the most popular three articles of all time?
select_query1 = """
    select path, count(*) as Views
        from log
    where path like '/article/%'
    group by path
    order by Views desc
    limit 3;
    """

#2. Who are the most popular article authors of all time?
select_query2 = """
    select authors.name, count(log) as views
        from authors
        left join articles
            on authors.id = articles.author
        left join log
            on log.path like concat('%', articles.slug, '%')
    group by authors.name
    order by views desc;
    """

#3. On which days did more than 1% of requests lead to errors?
select_query3 = """
    select *
        from (
            select to_char(log.time, 'yyyy-mm-dd') as date,
                round((sum(case when status = '404 NOT FOUND' then 1 else 0 end)::decimal / count(status)::decimal)*100,2) as percentage_errors
            from log
            group by date
        ) as t where percentage_errors >=1;
    """

# Store results
top_3_articles = dict()
top_3_articles['title'] = "\n1. What are the most popular three articles of all time?\n"

top_authors = dict()
top_authors['title'] = """\n2. Who are the most popular article authors of all time?\n"""

over_1p_errors = dict()
over_1p_errors['title'] = """\n3. On which days did more than 1% of requests lead to errors?\n"""


def get_results(query):
  db = psycopg2.connect(database=DBNAME)
  c = db.cursor()
  c.execute(query)
  results = c.fetchall()
  db.close()
  return results

def print_query_results(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + ' total views')

def print_error_query_results(query_result):
    print (query_result['title'])
    for result in query_result['results']:
        print ('\t' + str(result[0]) + ' - ' + str(result[1]) + ' % of requests')

# Store query result
top_3_articles['results'] = get_results(select_query1)
top_authors['results'] = get_results(select_query2)
over_1p_errors['results'] = get_results(select_query3)

# Print formatted output
print_query_results(top_3_articles)
print_query_results(top_authors)
print_error_query_results(over_1p_errors)
