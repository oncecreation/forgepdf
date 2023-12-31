initial_state = {
    'selected_pdf': '',
    'count': 0,
    'selected_pdf': '',
    'selected_pdfs': [],
    'current_frame': '',
    'preview_pdfs': []
}

class GlobalState:
    def __init__(self):
        self.data = initial_state

    def get_state(self, key):
        return self.data[key]
    
    def set_state(self, key, value):
        self.data[key] = value

    def reset_state(self):
        self.data = initial_state

class States:
    def __init__(self):
        self.COUNT = 'count'
        self.SELECTED_PDF = 'selected_pdf'
        self.SELECTED_PDFS = 'selected_pdfs'
        self.CURRENT_FRAME = 'current_frame'
        self.PREVIEW_PDFS = 'preview_pdfs'
    
state = GlobalState()
states = States()