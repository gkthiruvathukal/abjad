from experimental import *


def test_Menu_menu_entry_bodies_01():

    menu = scoremanagertools.menuing.Menu()
    menu._session.push_breadcrumb('location')
    tokens = ['apple', 'banana', 'cherry']
    section_1 = menu.make_section(tokens=tokens)
    section_1.title = 'section'
    tokens = [
        ('add', 'add something'),
        ('rm', 'delete something'),
        ('mod', 'modify something'),
        ]
    section_2 = menu.make_section(tokens=tokens)
    assert menu.menu_entry_bodies[-6:] == section_1.menu_entry_bodies + section_2.menu_entry_bodies
