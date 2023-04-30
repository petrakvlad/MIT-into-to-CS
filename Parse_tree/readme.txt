README
This is a Flask application that generates paraphrases for a given syntactic tree.

Installation
To run this application, you will need to have Python 3, flask and nltk installed on your machine. 

Usage
To use this application, you can run the file in the terminal, this will start the Flask server, which you can access by opening your web browser and navigating to http://localhost:5000/

Example of URL request (copy and paste to the browser in the running Flask app):
localhost:5000/paraphrase?tree=(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP
Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP
(JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ
trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS
restaurants) ) ) ) ) ) ) )


Endpoints
This application has the following endpoints:

GET /
Returns the message "Paraphrase application"

GET /paraphrase
Generates paraphrases for a given syntactic tree.

Parameters
tree: A string representation of a syntactic tree.
limit (optional): An integer specifying the maximum number of paraphrases to generate (default: 20).

Response
A JSON object containing a list of paraphrases.