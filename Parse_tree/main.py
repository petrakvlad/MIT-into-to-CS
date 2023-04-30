from flask import Flask, request, jsonify
import nltk
import itertools


app = Flask(__name__)

def paraphrase_tree(tree: str, limit: int = 20):
    # Convert the string 'tree' into an nltk.Tree object
    tree = nltk.Tree.fromstring(tree)

    # get first order children of the root node
    root_children = tree.subtrees(lambda t: t.label() == 'NP')
    # Initialize an empty dictionary to store the paraphrases
    paraphrases = {"paraphrases":[]}
    # Iterate through each root child node
    for each in root_children:
        # Check if the current node contains a comma or coordinating conjunction
        if any(i.label() == ',' or i.label() == 'CC' for i in each.subtrees()):
            # Retrieve all the child nodes that have the label 'NP'
            child_nps = [child for child in each if child.label() == 'NP']
             # Check if there are at least two child nodes with the label 'NP'
            if len(child_nps) > 1:
                # Generate all possible permutations of the 'NP' child nodes
                np_permutations = [child_nps]
                for i in range(2, len(child_nps) + 1):
                    np_permutations += list(itertools.permutations(child_nps, i))
                # Iterate through each permutation of 'NP' child nodes
                for permutation in np_permutations:
                    # Create a deep copy of the original tree
                    new_tree = tree.copy(deep=True)
                    # Replace the 'NP' child nodes in the current node with the permutation
                    np_node = each
                    np_node.set_label('NP')
                    np_node[:] = permutation
                    # Get the paraphrase as a string and remove newlines
                    paraphrase = str(new_tree).replace("\n", "")
                    # Check if the paraphrase is not already in the dictionary and add it
                    if paraphrase not in paraphrases:
                        paraphrases["paraphrases"].append({"tree": paraphrase})
                         # Check if the limit has been reached and break out of the loop
                        if len(paraphrases) >= limit:
                            break
            # Check if the limit has been reached and break out of the loop
            if len(paraphrases) >= limit:
                break

    # Return the dictionary of paraphrases
    return paraphrases


@app.route('/')
def home():
    return 'Paraphrase application'

@app.route('/paraphrase', methods=['GET'])
def paraphrase():
    # Parse query parameters
    tree_str = request.args.get('tree')
    if not tree_str:
        return jsonify({'error': 'Missing parameter "tree"'}), 400
    limit = int(request.args.get('limit', 20))

    # Generate paraphrases
    paraphrases = paraphrase_tree(tree_str, limit)

    # Return JSON response
    return jsonify({'paraphrases': paraphrases})

if __name__ == '__main__':
    app.run()