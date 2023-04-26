from flask import Flask, request, jsonify
from nltk.tree import Tree
from itertools import permutations

app = Flask(__name__)

def paraphrase_tree(tree_str, limit=20):
    # Parse the tree string into a Tree object
    tree = Tree.fromstring(tree_str)

    # Find all NP subtrees
    np_subtrees = tree.subtrees(lambda t: t.label() == "NP")

    # Generate permutations of the child NPs for each NP subtree
    paraphrases = []
    for np_subtree in np_subtrees:
        np_children = [child for child in np_subtree if child.label() == "NP"]
        if len(np_children) > 1:
            np_permutations = permutations(np_children)
            for np_permutation in np_permutations:
                paraphrase = tree.copy(deep=True)
                # Replace the original child NPs with the permuted ones
                for i, child in enumerate(np_subtree):
                    if child.label() == "NP":
                        paraphrase[paraphrase.leaf_treeposition(i)[:-1]] = np_permutation[i % len(np_permutation)]
                paraphrases.append(str(paraphrase))

    # Limit the number of paraphrases to be returned
    return paraphrases[:limit]

@app.route("/paraphrase", methods=["GET"])
def paraphrase():
    tree_str = request.args.get("tree", "")
    limit = int(request.args.get("limit", 20))
    paraphrases = paraphrase_tree(tree_str, limit)
    return jsonify(paraphrases)

@app.route('/')
def home():
    return 'Hello, World!'
    
if __name__ == "__main__":
    app.run(debug=True)
