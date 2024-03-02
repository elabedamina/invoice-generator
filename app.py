from flask import Flask, request, send_file
import jinja2
import pdfkit
import os
app = Flask(__name__)


@app.route('/generate_invoice', methods=['POST'])
def handle_generate_invoice():

    data = request.get_json()

    subtotal = 0
    products = []
    
    # Iterate over product data in the request payload
    for i in range(1, len(data) // 5 + 1):  
        product_id = data.get(f'product{i}_id')
        product_unit = data.get(f'product{i}_unit', '')
        product_name = data.get(f'product{i}_name', '')
        product_qty = int(data.get(f'product{i}_qty', 0))
        product_up = float(data.get(f'product{i}_up', 0))
        product_total = product_qty * product_up
        
        products.append({
            'product_id': product_id,
            'product_unit': product_unit,
            'product_name': product_name,
            'product_qty': product_qty,
            'product_up': product_up,
            'product_total': product_total
        })
        
        subtotal += product_total
    
    tax = subtotal * (data.get('tax_rate') / 100)
    total_price = subtotal + tax + data.get('freight', 0) + data.get('inssurance', 0) + data.get('legal_consular', 0) + data.get('inspection', 0) + data.get('other', 0)

    context = {
        "Company_Slogan": data.get('Company_Slogan'),
        "Street_Address": data.get('Street_Address'),
        "City_ZIP": data.get('City_ZIP', ''),
        "phone": data.get('phone', ''),
        "fix": data.get('fix', ''),
        "Date": data.get('Date'),
        "Expiration_Date": data.get('Expiration_Date'),
        "num_invoice": data.get('num_invoice'),
        "Name_Customer": data.get('Name_Customer'),
        "Company_Name_Customer": data.get('Company_Name_Customer'),
        "Address_Customer": data.get('Address_Customer'),
        "City_ZIP_Customer": data.get('City_ZIP_Customer'),
        "Phone_Customer": data.get('Phone_Customer'),
        "Name_Ship": data.get('Name_Ship'),
        "Company_Name_Ship": data.get('Company_Name_Ship'),
        "Address_Ship": data.get('Address_Ship'),
        "City_ZIP_Ship": data.get('City_ZIP_Ship'),
        "Phone_Ship": data.get('Phone_Ship'),
        "Air_Ocean": data.get('Air_Ocean'),
        "Est_Ship_Date": data.get('Est_Ship_Date'),
        "weight_units_Groos": data.get('weight_units_Groos', ''),
        "weight_units_Cubic": data.get('weight_units_Cubic', ''),
        "Total_Package": data.get('Total_Package', ''),
        "products":products,
        "subtotal": subtotal,
        "taxabale": subtotal,  
        "tax_rate": data.get('tax_rate', ''),
        "tax": tax,
        "freight": data.get('freight', ''),
        "inssurance": data.get('inssurance', ''),
        "legal_consular": data.get('legal_consular', ''),
        "inspection": data.get('inspection', ''),
        "other": data.get('other', ''),
        "total_price": total_price,
        "country_origins": data.get('country_origins', ''),
        "Port_Embarkation": data.get('Port_Embarkation', ''),
        "Port_Discharge": data.get('Port_Discharge', ''),
        "condition_payement": data.get('condition_payement', ''),
        "other_information": data.get('other_information', ''),
    }

    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    html_template = 'proforma_template.html'
    template = template_env.get_template(html_template)
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    output_pdf = 'proforma_template.pdf'
    pdfkit.from_string(output_text, output_pdf, configuration=config)

    if os.path.exists(output_pdf):
        return send_file(output_pdf, as_attachment=True, download_name='proforma_template.pdf'), 200
    else:
        return {'response': 'PDF generation failed'}, 500


if __name__ == '__main__':
    app.run(debug=True)