# n8n-Internship-Application-Workflow
An n8n-built automated pipeline that scrapes tech internship opportunity postings, filters on requirements, uploads results to a spreadsheet, and sends daily updates/reminders.

 ```mermaid
graph TD
    A[GitHub Internship List] --> B[n8n Scraper]
    B --> C[Regex Parser & Metadata Enrichment]
    C --> D[Deduplication & Prioritization]
    D --> E[Google Sheets/Airtable]
    D --> F[Slack/Discord Notifications]

<img width="560" height="315" alt="Screenshot 2025-09-23 at 12 03 34 AM" src="https://github.com/user-attachments/assets/6d84dca7-8378-456f-bb15-8cb699d1632e" />
