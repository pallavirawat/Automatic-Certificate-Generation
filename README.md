## Automatic Certificate Generation Using Gimp
It automatically generates certificates by taking input from a input file (can be txt) with names stored line by line.

## Prerequisites
GIMP and Python 2.7 installed

## Installation
1. Give permissions to "Automatic_Certificate_Generator.py" file. Use the command: <br />
        sudo chmod +x Automatic_Certificate_Generator.py
2. Copy "Automatic_Certificate_Generator.py" in /usr/lib64/gimp/2.x/plug-ins

Now to run it: <br />
1. Open Gimp. <br />
2. Navigate to Filters>Python-fu>CertificateGenerator <br /> <br />

A window will appear. In "certificate Template file" choose the template for your certificate. Sample certificate "template.xcf" is with the package.<br/>
In "Input Data File" choose the file in which your input data (Like names) is present.<br/>
And give the name for output folder (created relative to user home).<br/>
Thats it! Click OK and you're good to go.<br/>

