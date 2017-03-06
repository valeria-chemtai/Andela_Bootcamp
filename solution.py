def solution(num1,num2,operation):
	if (operation=="+"):
		return num1+num2
	if (operation=="-"):
		if num1>num2:
			return num1-num2
		else:
			return num2-num1
	if (operation=="*"):
		return num1*num2
	if (operation=="/"):
		return num1/num2