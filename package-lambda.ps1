# If you have a requirements.txt file, uncomment the line below
# pip install -r requirements.txt

# Step 3: Package for AWS Lambda
Remove-Item -Path ".\function.zip"
# Navigate to site-packages
Write-Host "Navigating to site-packages..."
cd .\venv\Lib\site-packages\

# Zip all the dependencies
Write-Host "Creating ZIP with dependencies..."
Compress-Archive -Path * -DestinationPath .\..\..\..\function.zip

# Navigate back to project directory
cd .\..\..\..\

# Add lambda function code to ZIP
Write-Host "Adding Lambda function code to ZIP..."
Compress-Archive -Path lambda_function.py, .\destinations\*, .\models\*, .\sources\* -Update -DestinationPath function.zip

Write-Host "ZIP file for AWS Lambda has been created!"
