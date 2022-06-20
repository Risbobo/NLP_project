#!/bin/bash
#SBATCH --job-name="test_model_NLP"
#SBATCH --time=02:00:00
#SBATCH --mem-per-cpu=8G
#SBATCH --partition=gpu
#SBATCH --qos=job_gpu_preempt
#SBATCH --gres=gpu:rtx2080ti:1
#SBATCH --no-requeue

# Your code below this line
#module load Python
#module load Anaconda3
srun python3 testAllModels.py
