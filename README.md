# n8n-Internship-Application-Workflow
An n8n-built automated pipeline that scrapes tech internship opportunity postings, filters on requirements, uploads results to a spreadsheet, and sends daily updates/reminders.

Currently sources postings from Pitt Github Internship postings. More Job board integrations coming soon. 
This implementation filters out jobs that are for Graduate students or require US citizenship. This can easily be changed by modifying the "Scrape and Filter Internships" code node.

The program is scheduled to run at 8:00am every day and send an email reminder that includes the number of job postings collected for that day. 

[!NOTE] n8n does not host its workflows on browser and requires a cloud service to host it

Current Workflow Diagram
<img width="533" height="340" alt="Screenshot 2025-09-23 at 12 20 17 AM" src="https://github.com/user-attachments/assets/66926d8d-0afc-4217-98c5-4b5ad18d5702" />
