python3 mr_decision_trees.py -r spark num_trees.txt > models.txt
python3 eval_decision_trees.py -r spark models.txt
