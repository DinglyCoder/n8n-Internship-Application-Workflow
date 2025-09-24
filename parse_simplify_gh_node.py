from bs4 import BeautifulSoup
import pprint

# remove body function header when using in n8n
def body(_input):
    # The Code node receives a list of input items. We'll process the first one.
    item = _input.all()[0]

    # The HTML content is now in the .text property from the HTTP Request node
    html_content = item.json["data"]
    soup = BeautifulSoup(html_content, 'html.parser')

    internships = []
    last_company = ''

    table_body = soup.find('tbody')
    if not table_body:
        return []

    for row in table_body.find_all('tr'):  
        cells = row.find_all('td')
        if len(cells) < 4:
            continue

        if cells[4].get_text(strip=True) != "0d":
            # reached end of internship for today. end search
            break
        # print(cells[4].get_text(strip=True))

        if "🇺🇸" in cells[1].get_text(strip=True):
            # role requires citizenship, skip
            continue

        if "🎓" in cells[1].get_text(strip=True):
            # role requires graduate student status, skip
            continue
        
        company_cell = cells[0]
        if '↳' in company_cell.get_text():
            current_company = last_company
        else:
            current_company = company_cell.get_text(strip=True)
            last_company = current_company

        role = cells[1].get_text(strip=True)
        location = cells[2].get_text(separator=', ', strip=True)
        link_tag = cells[3].find('a')
        application_link = link_tag['href'] if link_tag else 'N/A'

        internships.append({
            'company': current_company,
            'role': role,
            'location': location,
            'application_link': application_link,
        })

    # Return the final list of structured data
    return internships