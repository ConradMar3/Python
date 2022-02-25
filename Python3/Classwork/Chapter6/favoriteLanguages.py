favorite_languages = {
'conrad': ['react', 'python'],
'celeste': ['css3'],
'phil': ['math'],
'mariaan': ['BA', 'SQL'],
}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")

	for language in languages:
		print(f"\t{language.title()}")