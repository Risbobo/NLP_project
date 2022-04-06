#!/bin/bash
#SBATCH --job-name="First example"
#SBATCH --time=00:10:00
#SBATCH --mem-per-cpu=1G

# Your code below this line
module load Python
srun python3 main.py
