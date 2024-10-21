#!/bin/bash
mkdir bioinformatics_project
cd bioinformatics_project
mkdir data
mkdir scripts
mkdir results
cd scripts
touch generate_fasta.py
touch dna_operations.py
touch find_cutsites.py
cd .. 
cd results
touch cutsite_summary.txt
cd ..
cd data
touch random_sequence.fasta
cd ..

cat <<EOL > README.md 

Done with part 1 of midterm
EOL
echo "README.md has been created in the main project directory."
chmod +x setup_project.sh