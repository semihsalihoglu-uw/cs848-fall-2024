# Beyond Relational Systems (CS 848, Fall 2024)

## Logistics
+ **Instructor:** [Semih Salihoğlu](https://cs.uwaterloo.ca/~ssalihog/)
+ **Seminar Room:** DC 2568
+ **Seminar Time:** Wed 3-6pm

## Overview
Since the beginnings of computer science and in particular the field of data management,
several classes of data management systems have been developed to support different 
classes of applications. The most widely known of these are relational database managements
that implement the SQL query language and are based on the relational model of data.
Relational systems are widely known and have transformed the field of software engineering.
Yet, many classes of applications require different data models, query languages,
and/or computational capabilities from their underlying data or information systems.
This seminar will cover several of these classes of systems with a focus on applications
of these systems to AI. The main classes of systems we will cover are: 
- Datalog systems, which are based on the logic-based Datalog query language. We will cover several applications of Datalog
  to perform complex and declarative recursive querying over relational records. We will also cover
  very technical core query processing algorithms in Datalog.
- Resource description framework (RDF) systems, which are based on the RDF data model and 
the backbone of applications that use datasets that are nowadays referred to as "knowledge graphs". 
We will discuss the applications of RDF systems to AI, specifically symbolic AI, and do exercises
in automatic logical inferences that RDF systems can do.
- Property graph DBMSs, which are one of the most widely used database management
systems that propose a direct graph model instead of tabular model. We will discuss several core architectural
principles of developing property graph DBMSs and do exercises in graph querying.

The seminar is based on weekly paper readings and student presentations, discussions,
a term project, and several simple assignments that will give students a chance to work with
systems that we will cover. The most important part is the term project.

## Schedule
The below schedule is subject to change:
| Date | Topic | Readings | Assignments |
|:-----|:-----|:------------|:------------| 
| 4 Sep | Introduction, History of DBMSs (Semih lecturing) | <ul><li>[A Veritable Bucket of Facts](https://dl.acm.org/doi/10.1145/1147376.1147382) </li> <li>[Programmer As Navigator](https://dl.acm.org/doi/10.1145/355611.362534)</li> <li>[A Relational Model of Data for Large Shared Data Banks](https://dl.acm.org/doi/abs/10.1145/362384.362685)</ul> | |
| 11 Sep | Property Graph DBMSs 1 (Semih) | <ul><li>[The Ubiquity of Large Graphs User Survey](https://cs.uwaterloo.ca/~jimmylin/publications/Sahu_etal_VLDBJ2019.pdf) </li> <li>What's Graph DBMS Video [1](https://www.youtube.com/watch?v=BksVyv5864k&list=PLnMU6rfAdE1CpxwilWJyWETgy2J-KPkZj) [2](https://www.youtube.com/watch?v=sr63gtm1-j8&list=PLnMU6rfAdE1CpxwilWJyWETgy2J-KPkZj&index=2) <li> Modern Techniques For Querying Graph-structured Databases (see email) Chapter 1 until 2.3.2; Chapter 3 beginning until 3.3; Chapter 3.3.3; Chapter 4 until 4.2.2; Chapter 4.3.2 (skim through theoretical parts)</li> </ul>  | [A1](assignments/a1/a1.md) out (due Sep 25th) |
| 18 Sep | Parallel Graph Analytics Systems (Semih & Students) | <ul><li> [Pregel: A System for Large-scale Graph Processing](https://dl.acm.org/doi/10.1145/1807167.1807184) (Semih) </li> <li> [Ligra: A Lightweight Graph Processing Framework for Shared Memory](https://jshun.csail.mit.edu/ligra.pdf) (Mingkun) </li> | |
| 25 Sep | Datalog 1 (Semih) | [PDKBS](http://www.lsv.fr/~goubault/BD/ullman-principles-of-database-and-knowledge-base-systems-volume-1.pdf) Chapter 3 (from pgs 96 to 139 + 139-164 are optional but highly recommended) (For reviews: Provide a 2 page brief summary of the general formalism, semi-naive evaluation, and stratification) | [A2](assignments/a2/a2.md) out (due October 9) |
| 2 Oct | Datalog Applications (Students) | <ul> <li>[Strictly Declarative Specification of Sophisticated Points-to Analyses](https://yanniss.github.io/doop-oopsla09prelim.pdf) (Shaquille) </li> <li> [Declarative Routing: Extensible Routing With Declarative Queries](https://netdb.cis.upenn.edu/papers/declarenet.pdf) (Ruidi)</li> | |
| 9 Oct |  RDF 1 (Semih) | <ul> <li> [SWFWO](http://www.kevenlw.name/downloads/Ontologist.pdf) Chapter 3: Up to 31-51 + Blank Nodes (54-57); Chapter 5: 79-90; Chapter 6: 91-102; Chapter 7: 124-125 (Inverse), 129-132 (Symmetric Properties and Transitivity) (For reviews, provide a 2-page brief summary of the basics of RDF and some of the inferencing capabilities in these chapters with examples)  | A3 out (due October 23)|
| 16 Oct | Reading Week | | | |
| 23 Oct | RDF 2 (Students) | <ul> <li> [Linked Data Book](https://link.springer.com/book/10.1007/978-3-031-79432-2) Chapters 1, and 3 (no presentation, just reviews) <li> [DBPedia](https://www.researchgate.net/publication/259828897_DBpedia_-_A_Large-scale_Multilingual_Knowledge_Base_Extracted_from_Wikipedia) (Mayank) <li> [Google Dataset Search](https://dl.acm.org/doi/abs/10.1145/3308558.3313685) (Royi)  | |
| 30 Oct |  Vector Databases 1 (Semih) | <ul> <li> [SA-Tree](https://dl.acm.org/doi/10.1007/s007780200060) <li> [HNSW](https://arxiv.org/pdf/1603.09320) | |
| 6 Nov | Vector Databases 2 (Students) | <ul> <li> [HNSW](https://arxiv.org/pdf/1603.09320) (Diaa)  | |
| 13 Nov |Applications 1: Graph RAG (Students) (Shivani, Bishwajit) | <ul> <li> [Filtered DiskANN](https://harsha-simhadri.org/pubs/Filtered-DiskANN23.pdf) (Bishwajit) <li>[Hybrid RAG](https://arxiv.org/pdf/2408.04948) (Shivani) | |
| 20 Nov | Applications 2: Graph ML (Students) (Rui, Sterling)| <ul> <li> [node2Vec](https://arxiv.org/pdf/1607.00653) (Rui) <li> [RDF2Vec](https://madoc.bib.uni-mannheim.de/41307/1/Ristoski_RDF2Vec.pdf) (Sterling) | |
| 27 Nov | No Class | | |
| 4 Dec | Project presentations | | |

## Readings

This seminar's reading will cover chapters from the following surveys and textbooks in addition to research papers, which will be posted in the schedule.
+ [Semantic Web for the Working Ontologist (SWFWO)](https://tinyurl.com/2p9672s2), Allemang \& Hendler, 2008
+ Modern Query Processing Techniques for Graph Database Management Systems, 2024 (upcoming survey paper by Amine Mhedhbi, Amol Deshpande, and Semih Salihoğlu)
+ The Protégé Project: [1](https://perso.liris.cnrs.fr/amille/enseignements/MasterCode/IC_IA/session2/protege_evolution.pdf), [2](https://dl.acm.org/doi/pdf/10.1145/2757001.2757003)
+ [Principles of Database and Knowledge-Base Systems (PDKBS)](https://www.sti-innsbruck.at/sites/default/files/Knowledge-Representation-Search-and-Rules/principles-of-database-and-knowledge-base-systems-volume-1-1.pdf), Ullman, 1989


## Workload Breakdown
+ Class Participation: 15%
+ Paper Reviews + Assignments: 30%
+ Presentation: 10%
+ Project: 45%

## Paper Reviews
For the seminars where there is paper reading, we will be writing two reviews for two of the papers 
assigned to that day. If there are more than two papers assigned, you can pick any two of 
the assigned papers. You are not allowed to skip any reviews. Broadly, reviews should be critiques that interpret
why the paper is important and how it has contributed to the field (though see my detailed comment below). 
You have to finish your review with 
one question to start a discussion in the seminar. The reviews are due Tuesday midnight before the seminar
because I need to read them Wednesday morning as I prepare for the seminar and refer to them during the seminar.
You are expected to (very very) briefly answer the following 6 questions and finish your reviews with a
question that can start a discussion in class:

+ What is the problem?
+ Why is it important?
+ Why is it hard? Why don't previous methods work?
+ What is the solution to the problem the authors propose?
+ What interesting research questions does the paper raise?
+ (If related) How does the paper relate to other papers we have read?
The first 4 of these questions are from Jennifer 
Widom's [tips for writing introductions to technical papers](https://cs.stanford.edu/people/widom/paper-writing.html). 
I strongly recommend that each one of you read this entire document 
very carefully (probably multiple times) at some point in your graduate studies. There is no fixed format for the reviews 
but I recommend: Single column, 1.5 space, 12 pt, in Latex.

Ultimately, the main thing I am looking for is a demonstration of serious critical reading of the paper.

## Project Deliverables
There are three deliverables of your project, 1) a presentation in the last seminar; 2) a 6-page paper; and 3) the
source code of your project with instructions to run your code. The deadline for the paper and the code will be 
determined later.
+ Project Presentation: 15 minute long presentation, similar to your paper presentations and if appropriate a demo, in the last seminar.
+ Project Paper: The project papers will be 6 pages. You can have extra pages for the references.
They will be written in the two-column ACM proceedings format, using one of the ACM SIG Proceedings Templates.
+ Project Source Code: Please put your source code into github and include a link in your project writeup. 
On the github page, please document exactly how to run your source code.

The deadline for delivering the your project paper and source codes will be anounced later.
In addition by the 3rd week's seminar, everyone will submit a 1-page project proposal describing the scope of the project.
You can team up for your project or do one individually. You can be at most 2 people per project.

## Project Ideas
Here are several project ideas. You are welcome to come up with your own project ideas:
- Building a sophisticated-enough application using an RDF, Datalog, or property graph database. This can be building
a question and answering system that uses LLMs and RAG, a Datalog application, e.g., one that does declarative
networking as in these projects: [1](https://dl.acm.org/doi/pdf/10.1145/1592761.1592785) or [2](https://www2.eecs.berkeley.edu/Pubs/TechRpts/2009/EECS-2009-173.pdf).
- An experiment and analysis work evaluating the performance of LLMs on a beyond relational system, e.g.,
how accurate the queries generated by LLMs are (e.g., see [this paper](https://arxiv.org/pdf/2311.07509)) or
how accurate are LLMs in generating RDF triples from text documents?
- Doing a mini-research on a core component of an RDF or property graph database. For property graph
database I suggest using [Kùzu](https://github.com/kuzudb/kuzu). For RDF databases, we can discuss the options.
The core components could be storage manager, query processor, or the optimizer.
- A good project is to develop a very simple, in-memory, Datalog system that implements one core Datalog query processing algorithm
and the magic-sets optimization. This is a very good implementation-heavy project for people interested
in the internals of the system. A similar project can be done for RDF as well. The goals of such projects are to give
you a feel for the different core components of data management systems.

## Presentations
Each student will be doing 1 or 2 presentations in the term. The amount will depend on the class size. 
Each presentation will be about 25 minutes long. 
Here are the important points summarizing what you have to do for your presentations.

+ You must present with slides. The content in your slides should be your own but you can use others' materials, e.g., 
figures from the paper we are reading, when necessary and by crediting your source on your slide.
+ Please have a separate slide for each of 4 questions in the summary item in the Paper Review section.
+ It is very helpful to demonstrate the ideas in the paper through examples. So try to have examples in your presentation, e.g., a simulation of some code or system component.
