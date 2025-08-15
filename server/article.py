class Article:
    def __init__(self, page, title, sections):
        self.page = page
        self.title = title 
        self.sections = sections 
        
    def get_page(self):
        return self.page

    def get_title(self):
        return self.title

    def get_sections(self):
        return self.sections
