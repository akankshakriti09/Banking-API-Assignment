### Banking-API-Assignment
## Endpoints

* GET Bank List http://127.0.0.1:8000/bank-list/ - gets the list of all banks, page-wise

* GET Bank List with their branches http://127.0.0.1:8000/banklist-with-branches/ - gets the list of all banks with their branches and details of each branch, page-wise

* GET Branch List http://127.0.0.1:8000/branch-list/ - gets the list of all branches, page-wise

        ##### query params

        Search from branch name 
        Example: /branch-list?branch=branch_name - http://127.0.0.1:8000/branch-list/?branch=kolkata&main

        Search from bank name 
        Example: /branch-list?bank=bank_name - http://127.0.0.1:8000/branch-list/?bank=allahabad&bank
    

        Search for branches of that specific bank

        Example: /branch-list/?branch=branch_name&bank=bank_name - http://127.0.0.1:8000/branch-list/?branch=sindi&bank=allahabad&bank 
        These two can also be combined 

* GET http://127.0.0.1:8000/branch-list/4 : gets the branch with specific id of branch.

        Example request: /branches/4 returns a single object with following signature:

        {
            "url": "http://127.0.0.1:8000/branch-list/4/",
            "ifsc": "ABHY0065004",
            "branch": "BHANDUP",
            "bank_id": 60,
            "bank": "ABHYUDAYA COOPERATIVE BANK LIMITED",
            "address": "CHETNA APARTMENTS, J.M.ROAD, BHANDUP, MUMBAI-400078",
            "city": "MUMBAI",
            "district": "GREATER MUMBAI",
            "state": "MAHARASHTRA"
        }