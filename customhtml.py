from __future__ import division
import pytest,basicmath
from jinja2 import Environment
pytest.main()
testcasedetails=basicmath.maths().html
count=0
for dv in testcasedetails.values():
	if "Pass" in dv:
		count=count+1
total=len(testcasedetails)
algebrastatus=["Algebra",total,count,total-count,str(round((count/total)*100,2))]
try:
	with open("./template/index",'r') as templ:
		htmlval=templ.read()
		jinja_env=Environment().from_string(htmlval).render(title="Get Started with Jinja Template",header="Test Summary of Algebra",statusdet=algebrastatus,td=testcasedetails)
		with open("./reports/report.html",'w') as report:
			report.write(jinja_env)
except FileNotFoundError,IOError:
	print("File not found")

