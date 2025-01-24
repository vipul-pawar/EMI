from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import base64
from django.http import HttpResponseBadRequest

# Create your views here.

def emi_calculator_view(request):
    return render(request, 'calculator.html')

def result(request):
    # Ensure the request method is POST for sensitive data
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid request method.")

    # Get inputs and validate them
    principal = float(request.POST.get("principal", 0))
    annual_rate = float(request.POST.get("annual_rate", 0))
    tenure = int(request.POST.get("tenure", 0))

    if principal <= 0 or annual_rate <= 0 or tenure <= 0:
        return HttpResponseBadRequest("Invalid input. All values must be positive.")

    # EMI calculation
    monthly_rate = (annual_rate / 100) / 12
    emi = (principal * monthly_rate * (1 + monthly_rate)**tenure) / ((1 + monthly_rate)**tenure - 1)
    emi = round(emi, 2)

    # Total Paynment 
    total_payment = round((emi * tenure), 2)


    # Total interest payable
    total_interest = round((total_payment - principal), 2)

    # Generate the pie chart
    labels = ['Principal Loan Amount', 'Total Interest']
    values = [principal, total_interest]
    colors = ['#ff9999', '#66b3ff']

    plt.figure(figsize=(16, 9), dpi=125)  # Added to improve size issue
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, textprops={'fontsize': 20})
    plt.title('Loan Amount Breakdown', fontsize=24)

    # Save the chart to a BytesIO stream
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    chart_image = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()
    plt.close()

    # Pass only the required variables to the template
    context = { 
        "emi": emi,
        "total_payment": total_payment,
        "total_interest": total_interest,
        "chart_image": chart_image,  # Add the chart image to the context
    }

    return render(request, 'result.html', context)

def base (request):
    return render(request, 'base.html')
