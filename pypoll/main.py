import csv 
import os 
file_load = ("Resources/election_data.csv")
file_write = ("analysis/election_analysis.txt")
vote_count = 0
candidate =[]
votes= {}
winningcandidate=''



with open (file_load, 'r') as electiondata:  
   electiondata = csv.reader(electiondata)
   headers = next(electiondata)
   #print(electiondata)
   
   for r in electiondata:
      vote_count +=1

      candidate_name=r[2]

      if candidate_name not in candidate:
         candidate.append(candidate_name)
         votes[candidate_name]=0
      votes[candidate_name]+=1


   winningcandidate = max(zip(votes.values(), votes.keys()))[1]
   
   percentage = {key:round(((value / vote_count )*100 ),3)for key, value in votes.items()}

with open (file_write, 'w') as outputfile:  


   output1= (f'Election Results\n'
   f'-------------------------\n'
   f'Total Votes: {vote_count}\n'
   f'-------------------------\n')
   outputfile.write(output1)
   print(output1)
  
   for k,v in percentage.items():
      #print(k,v,votes[k])

      candidate_results = (
            f"{k}: {v}% ({votes[k]:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
      print(candidate_results)
        #  Save the candidate results to our text file.
      outputfile.write(candidate_results)

   
  
   output3=(f'-------------------------\n'
  f'Winner: {winningcandidate}\n'
  f'-------------------------') 
   print(output3)
   outputfile.write(output3)