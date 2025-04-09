```markdown
# FormFiller - Real Estate Data Collector

## 🎯 Project Description  
Automated solution for scraping property listings from Zillow-clone websites and populating Google Forms with extracted data.

## 📦 Deliverables  
- Web scraping module with BeautifulSoup  
- Google Forms automation using Selenium  
- Data cleaning pipeline  
- Headless browser integration  

## 🚀 Key Features  
- 🏠 Property data extraction (address/price/links)  
- 🤖 Automated form submission  
- 🔄 Batch processing of listings  
- 🛡️ Environment-based configuration  

## 🛠️ Technologies Used  
| Component              | Technology                          |
|------------------------|-------------------------------------|
| **Web Scraping**       | BeautifulSoup4                     |
| **Browser Automation** | Selenium                           |
| **Driver Management**  | webdriver-manager                  |
| **Env Management**     | python-dotenv                      |

## ⚙️ Installation & Setup  

### 1. Clone Repository  
```bash
git clone https://github.com/My-Py-Projects/filler-form
cd filler-form
```

### 2. Install Dependencies  
```bash
pip install requests beautifulsoup4 selenium webdriver-manager python-dotenv
```

### 3. Environment Configuration  
Create `.env` file:
```ini
FORMS_URL=your_google_form_url
```

### 4. Chrome Driver Setup  
Ensure Chrome browser is installed:
```bash
google-chrome --version  # Should be ≥ 114
```

### 5. Run Application  
```bash
python main.py
```

**Important Notes:**  
```plaintext
1. Form Requirements:
   - Must contain exactly 3 questions in this order:
     1. Address
     2. Price
     3. Link

2. Customization Points:
   - Update CSS selectors if website changes
   - Modify XPATHs for different form structures
   
3. Data Visualization:
   - Responses are automatically saved to Google Sheets when linked
   - Enable in Form settings: 'Responses' → Link to Sheets
```