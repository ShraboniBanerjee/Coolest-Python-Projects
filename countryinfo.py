from countryinfo import CountryInfo
count=input("Enter your country : ")
country = CountryInfo(count)
print("Capital is : ",country.capital())
print("Borders  : ",country.borders())
print("Language is : ",country.languages())
print("Currencies : ",country.currencies())
print("Other Names : ",country.alt_spellings())