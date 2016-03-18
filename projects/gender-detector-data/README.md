Automated Gender Analysis of Carnegie Museum of Art

Introduction

Carnegie Museum of Art is a prestigious museum of contemporary art in Pittsburgh, Philadelphia. Art, generally, is a male-dominated profession and a male-dominated world, but this has begun to slowly change, since the feminist movements of the mid-1900s. This gender analysis shows that in the years between 1960 and 1980, only 8 percent of the Carnegie Museum of Art's new collected objects in this time were produced by female artists. In the years between 1995 and 2015, only 21 percent of the new collected objects in this time were produced by female artists. I chose these date spans because I wanted both date spans to feel contemporary, and I wanted them to correspond with the vast amount of change that has occurred in the art world from the 1960s and 70s to today in the 2000s. I expected the change in percentage of work by female artists acquired to be a dramatic one.

The results agreed with my more general hypothesis that the percentage of women artists collected would increase from the twenty year span 1960-1980 to the twenty year span 1995-2015. It did not line up with my expectation that the collected objects between 1995 and 2015 would include a vastly larger percentage of women as producers, maybe 35% or more, than the percentage that my analysis demonstrated, 21%. 

Methodology

I analyzed one json file filled with information about each object in the Carnegie's collection.

The methodology of the gender detection is similar to that of the babynames-gender-detector homework.

Difficulties inherent in my dataset included the fact that many of the names are international, or that first initials are used as first names in the document. My gender detector uses American baby names, and this made the gender detecting a less confident process. Other smaller difficulties included that dates included the months, not just the years. I was able to wrangle the data into a csv document that included only years of the dates, and only first names from the names category, which made the data more usable.

Past Research and Articles

I was particularly inspired towards this project topic by this "Guerilla Girls" poster: 
http://blogs.elespectador.com/parsimonia/files/2015/04/Guerrilla-girls-museos.jpg
The Guerilla Girls are a contemporary group that works to raise awareness of inequality of representation in the art world. Here is an article about them, which includes some of their awesome and clever political posters. http://www.sparksummit.com/2014/09/09/spark-artists-the-guerrilla-girls-and-activism-as-art/


I also took a class this quarter called Feminism and Contemporary Art, where we learned much about the underrepresentation of women and minorities in art and art history, and the challenges inherent in gender or race posed to artists who are not white and male. This was my awesome textbook for that class: https://en.wikipedia.org/wiki/WACK!_Art_and_the_Feminist_Revolution

I saw that this person had done some cool visualization with gender and the MoMA dataset, which I did not use for this project because it included gender already in the dataset: https://twitter.com/EamonCaddigan/status/626861365546848256
And some other things people have done with MoMA's dataL:
https://medium.com/@foe/here-s-a-roundup-of-how-people-have-used-our-data-so-far-80862e4ce220#.2qfkw3cis

Some other news clips:
http://www.theguardian.com/lifeandstyle/the-womens-blog-with-jane-martinson/2013/may/24/women-art-great-artists-men
http://nymag.com/arts/art/features/40979/
https://nbmaa.wordpress.com/2010/12/03/are-women-still-a-minority-in-art-museums/

How to use it

fetch_data.py - Running this script will download one large json file from Carnegie Museum of Art's Github page and store them in data/

wrangle_data.py - Running this script will create a new, smaller csv file that includes all of the objects in the collection, and the following information about each one. These are all the headers of the csv file: 'title', 'creation_date', 'date_acquired', 'cited_name', 'party_type'

fetch_gender_data.py - Running this script will download lists of all babynames recorded from www.ssa.gov

wrangle_gender_data.py - Running this script will make a csv file with all the baby names and the following information about them (headers): 'name', 'gender' , 'ratio' , 'females', 'males', 'total'

gender.py - this script defines detect_gender() function

classify.py - Running this script will use detect_gender() to rewrite the wrangled data csv file to include three more headers - gender of each artist name, ratio (how skewed it is towards one gender over another), and usable name, which is just the artist's first name. After running this script, the csv file will include: 'title', 'creation_date', 'date_acquired', 'cited_name', 'party_type', 'ratio', 'gender', 'usable_name'

analyze.py - Running this script will analyze the data in the three ways I have chosen - first, it computes the overall percentage of work by female artists acquired by the Carnegie Museum of Art. Then, it analyzes what percentage of work by female artists was acquired in the years 1960-1980, and the percentage of work by female artists acquired in the years 1995-2015.

Analysis

First, I computed that the overall percentage of work by female artists acquired by the Carnegie Museum of Art was 12%. Then, I computed that the percentage of work by female artists  acquired in the years 1960-1980 was 8%, and the percentage of work by female artists acquired in the years 1995-2015 was 21%.





