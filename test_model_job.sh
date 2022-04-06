#!/bin/bash
#SBATCH --job-name="test_model_NLP"
#SBATCH --time=00:30:00
#SBATCH --mem-per-cpu=4G

# Your code below this line
module load Python
srun python3 test_model.py
