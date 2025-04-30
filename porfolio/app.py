"""
Author: Anna (Anya) Vlasova
"""
# general
from flask import Flask, request, session, redirect, url_for
import pyhtml as h
import requests
from pyhtml import script

app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
def homepage():
    '''
    Main page
    '''
    response = h.html(h.head(
                h.link(rel="preconnect", href="https://fonts.googleapis.com"),
                h.link(rel="preconnect", href="https://fonts.gstatic.com"),
                h.link(href="https://fonts.googleapis.com/css2?family=Rubik+Dirt&family=Rubik:ital,wght@0,300..900;1,300..900&family=Titan+One&display=swap", rel="stylesheet"),
                h.link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded"),
                h.title("Anya's Portfolio"),
                h.link(rel='stylesheet', href='static/style.css')),
                h.body(
                    h.ul(id='navbar')(h.li(h.a('Welcome', href = '#welcome')),
                         h.li(h.a('About me', href = '#about')),
                         h.li(h.a('Skills', href = '#skills')),
                         h.li(h.a('Projects', href = '#projects')),
                         h.li(id='logo')("Anya's Portfolio")),


                    h.div(id='welcome')(
                    h.div(id='image+text')(
                        h.p(id='undertext')('PORTFOLIO PORTFOLIO PORTFOLIO PORTFOLIO')),
                        h.img(id='profileimage')(src=url_for('static', filename='profile_photo.jpg')),
                    h.div(class_='text', id='welcometext')(
                    h.h1(id='jumpy')(h.span('W'), h.span('E'), h.span('L'), h.span('C'), h.span('O'), h.span('M'),h.span('E'),),
                    h.br,
                    h.h2(id='message')('My name is Anya & I am an emerging UI/UX designer, currently studying in UNSW. I aim to make my projects practical & functional, while keeping it engaging & joyful. In my design process, I rely on research & evidence, to create truly human-centred solutions.')))),


                    h.div(id='about')(h.h1(class_='heading')('ABOUT ME'),
                                      h.br,
                                      h.div(class_='columns')(
                                    h.div(class_='text')(
                                          h.h2(class_='dark')('Education'),
                                          h.br,
                                          h.div(class_='text-row')(
                                          h.i(class_='material-symbols-rounded')('emergency'),
                                          h.h3(class_='yearsd')('2023-currently'),
                                          h.h3('UNSW')),
                                          h.div(class_='text-row')(
                                          h.i(class_='material-symbols-rounded')('more_vert'),
                                          h.h4('Bachelor of Design')),
                                        h.div(class_='text-row')(
                                          h.i(class_='material-symbols-rounded')('emergency'),
                                          h.h3(class_='yearsd')('2020-2023'),
                                          h.h3('National Research University Higher School of Economics (HSE)')),
                                          h.div(class_='text-row')(
                                          h.h4(class_='move')('Bachelor of Philology')),
                                          h.br,
                                          h.h2(class_='dark')('Hobbies'),
                                          h.br,
                                          h.i(class_='material-symbols-rounded', id='icon')('menu_book'),
                                          h.i(class_='material-symbols-rounded', id='icon')('content_cut'),
                                          h.i(class_='material-symbols-rounded', id='icon')('checkroom'),
                                          h.i(class_='material-symbols-rounded', id='icon')('footprint'),
                                          h.br,
                                          h.div(class_='text-row')(
                                          h.h4(class_='hobbies_text')('reading'),
                                          h.h4(class_='hobbies_text')('crafts'),
                                          h.h4(class_='hobbies_text')('styling'),
                                          h.h4(class_='hobbies_text')('exploring')),
                                          ),
                                    h.div(class_='side')
                                    (h.img(class_='image', id='sidephoto')(src=url_for('static', filename='sideprofile.png'))),


                                      h.div(id='stickynote')(
                                          h.div(class_='text')(
                                          h.h2(class_='light')('Activities'),
                                          h.br,h.br,
                                        h.div(class_='text-row')(
                                          h.i(class_='material-symbols-rounded')('emergency'),
                                          h.h3(class_='yearsl')('2025'),
                                          h.h3(class_='onblue')('Career Discovery Mentoring Program')),
                                          h.div(class_='text-row')(
                                          h.h4(class_='move')('5 meetings with UI/UX mentor')),
                                        h.br,
                                        h.div(class_='text-row')(
                                          h.i(class_='material-symbols-rounded')('emergency'),
                                          h.h3(class_='yearsl')('2025'),
                                          h.h3(class_='onblue')('Terrible Ideas Hackathon')),
                                          h.div(class_='text-row')(
                                          h.h4(class_='move')('3-day intensive prototyping')),
                                        h.br,
                                        h.div(class_='text-row')(
                                          h.i(class_='material-symbols-rounded')('emergency'),
                                          h.h3(class_='yearsl')('2025'),
                                          h.h3(class_='onblue')('Leadership Foundation')),
                                          h.div(class_='text-row')(
                                          h.h4(class_='move')('developing self-awareness and leadership skills')),
                                        h.br,
                                        h.div(class_='text-row')(
                                          h.i(class_='material-symbols-rounded')('emergency'),
                                          h.h3(class_='yearsl')('2025'),
                                          h.h3(class_='onblue')('Innovator Pro')),
                                          h.div(class_='text-row')(
                                          h.h4(class_='move')('measuring Waverley Counsel engagement in a multi-disciplinary team ')),
                                          h.br,
                                          h.div(class_='text-row')(
                                          h.i(class_='material-symbols-rounded')('emergency'),
                                          h.h3(class_='yearsl')('2024'),
                                          h.h3(class_='onblue')("Undergraduate Dean's List of 2024")),
                                          h.div(class_='text-row')(
                                          h.h4(class_='move')('outstanding Academic Excellence')),
                                          ))
                                      )),



                    h.div(id='skills')(h.h1(class_='heading', id='black')('SKILLS'),
                    h.div(class_='threecolumns')(
                    h.div(class_='column')(
                    h.h2(class_='subheading')('Soft skills'),
                    h.div(class_='skill_div')(
                    h.p(class_='skill_list')('written & oral communication'),
                    h.p(class_='skill_list')('teamwork & flexibility'),
                    h.p(class_='skill_list')('problem solving'),
                    h.p(class_='skill_list')('critical thinking'))),
                    h.div(class_='column')(
                    h.h2(class_='subheading')('Hard skills'),
                    h.div(class_='skill_div')(
                    h.p(class_='skill_list')('wireframing'),
                    h.p(class_='skill_list')('prototyping'),
                    h.p(class_='skill_list')('HTML & CSS'),
                    h.p(class_='skill_list')('layout & composition'),
                    h.p(class_='skill_list')('user testing'))),
                    h.div(class_='column')(
                    h.br,
                    h.h2(class_='subheading')('Software'),
                    h.div(class_='software-row')(
                    h.img(class_='software')(src=url_for('static', filename='figma.png')),
                    h.img(class_='software')(src=url_for('static', filename='vscode.webp')),
                    h.img(class_='software')(src=url_for('static', filename='indesign.png')),
                    h.img(class_='software')(src=url_for('static', filename='illustrator.png'))),
                    )),
                    h.div(id='stars')(
                    h.i(class_='material-symbols-rounded', id='decor')('emergency'),
                    h.i(class_='material-symbols-rounded', id='decor')('emergency'),
                    h.i(class_='material-symbols-rounded', id='decor')('emergency'))),




                    h.div(id='projects')(h.h1(class_='heading')('PROJECTS'),
                    h.br)(h.div(class_='bubble')
                (h.br,
                 h.div(class_='for_rows')(
                h.div(class_='image-row')(
                    h.img(class_='image')(src=url_for('static', filename='first_app_1.png')),
                    h.img(class_='image')(src=url_for('static', filename='first_app_2.png'))),
                    h.div(class_='image-row')(
                    h.img(class_='image', id='exception')(src=url_for('static', filename='first_app_web.png')))),
                        h.div(class_='text')
                        (h.h2(class_='projectname')('Group Project Portal'), h.br,
                        h.p('My first UI/UX design project, concentrated on proper design process: research, user testing of existing apps, pain-point identification and then iterative wireframing, considering user feedback. Additionally, it required ecosystem thinking to ensure that web and app versions both comply to Nielsen’s heuristics.'),
                        h.br,
                        h.div(class_='skill_div')(
                        h.p(class_='skill_list')('research'),
                        h.p(class_='skill_list')('user testing'),
                        h.p(class_='skill_list')('Adobe XD')),
                        h.br,
                        h.div(class_='button_container')(
                        h.a(h.button(class_='button')('Learn more.'), href='/Group_Project_Portal')))),


                    (h.div(class_='bubble')
                (h.br,
                h.img(class_='image')(src=url_for('static', filename='Pentapack_website_1.jpg')),
                h.img(class_='image')(src=url_for('static', filename='Pentapack_website_2.jpg')),
                    h.div(class_='text')
                    (h.h2(class_='projectname')('PentaPACK Website'), h.br,
                    h.p('This website consists of a main page and B2B communication section for an imaginary company. As a part of bigger team, I had to work under restrictions of existing brand identity, ensuring that brand’s individuality is not sacrificed for usability and vice versa.'),
                    h.br,
                    h.div(class_='skill_div')(
                    h.p(class_='skill_list')('Figma'),
                    h.p(class_='skill_list')('existing brand identity'),
                    h.p(class_='skill_list')('one-page layout')),
                    h.br,
                        h.div(class_='button_container')(
                        h.a(h.button(class_='button')('Learn more.'), href='/PentaPack_website')))),


                (h.div(class_='bubble')
                (h.br,
                h.div(class_='for_rows')(
                h.div(class_='image_row')(
                h.img(class_='image')(src=url_for('static', filename='covid19_1.png')),
                h.img(class_='image')(src=url_for('static', filename='covid19_2.png')),
                h.img(class_='image')(src=url_for('static', filename='covid19_3.png')))),
                    h.div(class_='text')
                    (h.h2(class_='projectname')('COVID19 App'), h.br,
                    h.p('This app is a quick response to the context of COVID19. It is aimed at restoring connections cut during the lockdown, when some people were apart, while others had to remain together. Using five love languages and alone time users are able to communicate their needs to their partner, regardless of distance.'),
                    h.br,
                    h.div(class_='skill_div')(
                    h.p(class_='skill_list')('fast prototyping'),
                    h.p(class_='skill_list')('Figma'),
                    h.p(class_='skill_list')('ethical considerations')),
                    h.br,
                        h.div(class_='button_container')(
                        h.a(h.button(class_='button')('Learn more.'), href='/Covid19_app')))),


                (h.div(class_='bubble')
                (h.br,
                h.div(class_='for_rows')(
                h.div(class_='image-row')(
                h.img(class_='image')(src=url_for('static', filename='graphics_1.png')),
                h.img(class_='image')(src=url_for('static', filename='graphics_2.png'))),
                h.div(class_='image-row')(
                h.img(class_='image')(src=url_for('static', filename='graphics_3.png')),
                h.img(class_='image')(src=url_for('static', filename='graphics_4.png')))),
                    h.div(class_='text')
                    (h.h2(class_='projectname')('Publication Design'), h.br,
                    h.p('This publication design combines mark making, photography, manipulated images and paper collages in order to support the articles’s message with graphic language. My goal was to allow the style of the publication blend contemporary and 1930s aesthetics, to highlight the  timeless relevance of the writing.'),
                    h.br,
                    h.div(class_='skill_div')(
                    h.p(class_='skill_list')('InDesign'),
                    h.p(class_='skill_list')('graphic design'),
                    h.p(class_='skill_list')('layout')),
                    h.br,
                        h.div(class_='button_container')(
                        h.a(h.button(class_='button')('Learn more.'), href='/Publication_design'))))),


                (h.div(class_='bubble')
                (h.br,
                h.div(class_='for_rows')(
                h.div(class_='image-row')(
                h.img(class_='image', id='exception')(src=url_for('static', filename='coding_3.png'))),
                h.div(class_='image-row')(
                h.img(class_='image')(src=url_for('static', filename='coding_1.png')),
                h.img(class_='image')(src=url_for('static', filename='coding_2.png')))),
                    h.div(class_='text')
                    (h.h2(class_='projectname')('Coded MyBASKET Website'), h.br,
                    h.p('The website fully coded by me. Using APIs, it retrieves prices from main grocery shops and analyses where your overall basket will be cheaper.'),
                    h.br,
                    h.div(class_='skill_div')(
                    h.p(class_='skill_list')('HTML'),
                    h.p(class_='skill_list')('Python'),
                    h.p(class_='skill_list')('CSS')),
                    h.br,
                        h.div(class_='button_container')(
                        h.a(h.button(class_='button')('Learn more.'), href='/Coded_website'))))),


                (h.div(class_='bubble')
                (h.br,
                h.div(class_='for_rows')(
                h.div(class_='image-row')(
                h.img(class_='image', id='exception')(src=url_for('static', filename='overall.png'))),
                h.div(class_='image-row')(
                h.img(class_='image')(src=url_for('static', filename='bug_hotel.png')),
                h.img(class_='image')(src=url_for('static', filename='camera_flowers.png')))),
                    h.div(class_='text')
                    (h.h2(class_='projectname')('Preservation project'), h.br,
                    h.p('A fully natural solution for the Southern bent-wing bat preservation. As one of their main concerns is decline in food sources, I proposed using night-blooming flowers, water sources and bug hotels to attract moths to the area and allow them to breed.'),
                    h.br,
                    h.div(class_='skill_div')(
                    h.p(class_='skill_list')('Blender'),
                    h.p(class_='skill_list')('system thinking'),
                    h.p(class_='skill_list')('bio-inspired design')),
                    h.br,
                        h.div(class_='button_container')(
                        h.a(h.button(class_='button')('Learn more.'), href='/Preservation_project')))))

                    )
                ) # type: ignore
    ))
    return str(response)


@app.route('/Group_Project_Portal', methods = ['GET', 'POST'])
def Group_Project_Portal():
    '''
    Project page.
    '''
    response = h.html(h.head(
                h.link(rel="preconnect", href="https://fonts.googleapis.com"),
                h.link(rel="preconnect", href="https://fonts.gstatic.com"),
                h.link(href="https://fonts.googleapis.com/css2?family=Rubik+Dirt&family=Rubik:ital,wght@0,300..900;1,300..900&family=Titan+One&display=swap", rel="stylesheet"),
                h.link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&icon_names=emergency"),
                h.title("Anya's Portfolio"),
                h.link(rel='stylesheet', href='static/style.css')),
                h.body(class_='black')(
                    h.ul(id='navbar')(h.li(h.a('Welcome', href = '/#welcome')),
                         h.li(h.a('About me', href = '/#about')),
                         h.li(h.a('Skills', href = '/#skills')),
                         h.li(h.a('Projects', href = '/#projects')),
                         h.li(id='logo')("Anya's Portfolio")),
                    h.div(class_='container')(
                    h.div(class_='grid_menu')(
                        h.ul(h.li(h.a('Problem or Task', href = '#problem'),
                                h.li(h.a('Research', href = '#research')),
                                h.li(h.a('Solution', href = '#solution')),
                                h.li(h.a('Space for Improvement', href = '#improvement')),
                                h.li(h.a('What I Learned', href = '#learning')))),
                    ),
                    h.div(class_='grid_main')(
                    h.h1(class_='heading')('Group Project Portal'),
                    h.br,
                    h.div(class_='beginning')(
                    h.div(class_='for_left')(
                        h.img(class_='portret')(src=url_for('static', filename='first_app_1.png')),
                        h.img(class_='portret')(src=url_for('static', filename='first_app_2.png'))),
                    h.div(class_='for_right')(
                        h.br,
                        h.h3('Time: '), h.h4('2.5 months.'),
                        h.br,
                        h.h3('Project Style: '), h.h4('individual.'),
                        h.br,
                        h.h3('Tools: '), h.h4('Adobe XD.'),
                        h.br, h.h4('My first UI/UX design project, concentrated on proper design process: research, user testing of existing apps, pain-point identification and then iterative wireframing, considering user feedback. Additionally, it required ecosystem thinking to ensure that web and app versions both comply to Nielsen’s heuristics.'))),
                    h.div(class_='project_description')(
                    h.h2(id='problem', class_='subheading')('Problem or Task'),
                    h.p('After conducting critical research of two graphical user interfaces and experiences (Trello and Notion), the identified issues had to be resolved in original design.'),
                    h.h2(id='research', class_='subheading')('Research'),
                    h.h3('1) empathy map'),
                    h.img(class_='landscape')(src=url_for('static', filename='empathy_map.png')),
                    h.h3('2) user journey'),
                    h.img(class_='landscape')(src=url_for('static', filename='Trello_journey.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='Notion_journey.png')),
                    h.h3('3) heuristic evaluation'),
                    h.img(class_='landscape')(src=url_for('static', filename='Trello_heuristics.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='Notion_heuristics.png')),
                    h.h3('4) ideating UI/UX solution'),
                    h.img(class_='landscape')(src=url_for('static', filename='issues_1.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='issues_2.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='issues_3.png')),
                    h.h3('5) considering ecosystem'),
                    h.img(class_='landscape')(src=url_for('static', filename='ecosystem.png')),
                    h.h3('6) prototype and user test'),
                    h.img(class_='landscape')(src=url_for('static', filename='midfi.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='testing_1.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='testing_2.png')),
                    #h.img(class_='landscape')(src=url_for('static', filename='.png')),
                    h.h3('7) high fidelity interactive prototype'),
                    h.img(class_='landscape')(src=url_for('static', filename='final_1.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='final_2.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='final_3.png')),
                    h.h2(id='solution', class_='subheading')('Solution'),
                    h.img(class_='portret')(src=url_for('static', filename='first_app_1.png')),
                    h.img(class_='portret')(src=url_for('static', filename='first_app_2.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='first_app_web_2.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='first_app_web_3.png')),
                    h.h3('Walk through:'),
                    h.video(class_='portret', controls=True)(src=url_for('static', filename='phone final.mp4')),
                    h.video(class_='landscape', controls=True)(src=url_for('static', filename='final PC shorter.mp4')),
                    h.h2(id='improvement', class_='subheading')('Space for Improvement'),
                    h.p('If I had more time:'),
                    h.ul(class_='list')(h.li('More details & depth to the elements.'),
                         h.li('Web page organisation.'),
                         h.li('User test more often throughout the process.')),
                    h.h2(id='learning', class_='subheading')('What I Learned'),
                    h.ul(class_='list')(h.li('UI iterative design process: empathy mapping, analysis of user journey, prototyping with regular user testing, creating high fidelity design.'),
                         h.li('The importance of user testing and feedback.'),
                         h.li('Thinking of ecosystem: how web and app design should correspond to each other.'))
                    ),
                ))
    ))
    return str(response)

@app.route('/PentaPack_website', methods = ['GET', 'POST'])
def PentaPack_website():
    '''
    Project page.
    '''
    response = h.html(h.head(
                h.link(rel="preconnect", href="https://fonts.googleapis.com"),
                h.link(rel="preconnect", href="https://fonts.gstatic.com"),
                h.link(href="https://fonts.googleapis.com/css2?family=Rubik+Dirt&family=Rubik:ital,wght@0,300..900;1,300..900&family=Titan+One&display=swap", rel="stylesheet"),
                h.link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&icon_names=emergency"),
                h.title("Anya's Portfolio"),
                h.link(rel='stylesheet', href='static/style.css')),
                h.body(class_='black')(
                    h.ul(id='navbar')(h.li(h.a('Welcome', href = '/#welcome')),
                         h.li(h.a('About me', href = '/#about')),
                         h.li(h.a('Skills', href = '/#skills')),
                         h.li(h.a('Projects', href = '/#projects')),
                         h.li(id='logo')("Anya's Portfolio")),
                    h.div(class_='container')(
                    h.div(class_='grid_menu')(
                        h.ul(h.li(h.a('Problem or Task', href = '#problem'),
                                h.li(h.a('Research', href = '#research')),
                                h.li(h.a('Solution', href = '#solution')),
                                h.li(h.a('Space for Improvement', href = '#improvement')),
                                h.li(h.a('What I Learned', href = '#learning')))),
                    ),
                    h.div(class_='grid_main')(
                    h.h1(class_='heading')('PentaPACK Website'),
                    h.br,
                    h.div(class_='beginning')(
                    h.div(class_='for_left')(
                        h.img(class_='portret')(src=url_for('static', filename='Pentapack_shorter.png'))),
                    h.div(class_='for_right')(
                        h.br,
                        h.h3('Time: '), h.h4('3-4 weeks.'),
                        h.br,
                        h.h3('Project Style: '), h.h4('individual part of a group project.'),
                        h.br,
                        h.h3('Tools: '), h.h4('Figma.'),
                        h.br, h.h4('This website consists of a main page and B2B communication section for an imaginary company. As a part of bigger team, I had to work under restrictions of existing brand identity, ensuring that brand’s individuality is not sacrificed for usability and vice versa.'))),
                    h.div(class_='project_description')(
                    h.h2(id='problem', class_='subheading')('Problem or Task'),
                    h.p('To create the main page and B2B communication page for an imaginary company, providing sustainable packaging services.'),
                    h.h2(id='research', class_='subheading')('Research'),
                    h.p('To work with the new format of one-page website, I have researched similar websites, their interactions and menu organisation. A small user testing was conducted to see what layout was better.'),
                    h.img(class_='landscape')(src=url_for('static', filename='PentaPack_navbar.png')),
                    h.h2(id='solution', class_='subheading')('Solution'),
                    h.img(class_='portret')(src=url_for('static', filename='Pentapack_website_1.jpg')),
                    h.img(class_='portret')(src=url_for('static', filename='Pentapack_website_2.jpg')),
                    h.h2(id='improvement', class_='subheading')('Space for Improvement'),
                    h.p('If I had more time:'),
                    h.ul(class_='list')(h.li('More comprehensive user testing.'),
                         h.li('Incorporating details that highlight brand individuality throughout the website.'),
                         h.li('Better support of text with imagery and diagrams.')),
                    h.h2(id='learning', class_='subheading')('What I Learned'),
                    h.ul(class_='list')(h.li('Working on an individual part in a team, where my progress depended on others.'),
                         h.li('One-page web design.'),
                         h.li('Incorporating existing brand identity.'))
                    ),
                ))
    ))
    return str(response)


@app.route('/Covid19_app', methods = ['GET', 'POST'])
def Covid19_app():
    '''
    Project page.
    '''
    response = h.html(h.head(
                h.link(rel="preconnect", href="https://fonts.googleapis.com"),
                h.link(rel="preconnect", href="https://fonts.gstatic.com"),
                h.link(href="https://fonts.googleapis.com/css2?family=Rubik+Dirt&family=Rubik:ital,wght@0,300..900;1,300..900&family=Titan+One&display=swap", rel="stylesheet"),
                h.link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&icon_names=emergency"),
                h.title("Anya's Portfolio"),
                h.link(rel='stylesheet', href='static/style.css')),
                h.body(class_='black')(
                    h.ul(id='navbar')(h.li(h.a('Welcome', href = '/#welcome')),
                         h.li(h.a('About me', href = '/#about')),
                         h.li(h.a('Skills', href = '/#skills')),
                         h.li(h.a('Projects', href = '/#projects')),
                         h.li(id='logo')("Anya's Portfolio")),
                    h.div(class_='container')(
                    h.div(class_='grid_menu')(
                        h.ul(h.li(h.a('Problem or Task', href = '#problem'),
                                h.li(h.a('Research', href = '#research')),
                                h.li(h.a('Solution', href = '#solution')),
                                h.li(h.a('Space for Improvement', href = '#improvement')),
                                h.li(h.a('What I Learned', href = '#learning')))),
                    ),
                    h.div(class_='grid_main')(
                    h.h1(class_='heading')('Covid19 App'),
                    h.br,
                    h.div(class_='beginning')(
                    h.div(class_='for_left')(
                        h.img(class_='portret')(src=url_for('static', filename='covid19_1.png')),
                        h.img(class_='portret')(src=url_for('static', filename='covid19_2.png'))),
                    h.div(class_='for_right')(
                        h.br,
                        h.h3('Time: '), h.h4('3 weeks.'),
                        h.br,
                        h.h3('Project Style: '), h.h4('individual.'),
                        h.br,
                        h.h3('Tools: '), h.h4('Figma.'),
                        h.br, h.h4('This app is a quick response to the context of COVID19. It is aimed at restoring connections cut during the lockdown, when some people were apart, while others had to remain together. Using five love languages and alone time users are able to communicate their needs to their partner, regardless of distance.'))),
                    h.div(class_='project_description')(
                    h.h2(id='problem', class_='subheading')('Problem or Task'),
                    h.p('An app that responds to the context of COVID19.'),
                    h.h2(id='research', class_='subheading')('Research'),
                    h.p('The main exploration done for this project was design consideration. I have analysed: '),
                    h.ul(class_='list')(h.li('social consideration: human interactions are put at the core of the design;'),
                         h.li('behavioural consideration: people behaviour in lockdown was examined;'),
                         h.li('ethics: mental health activities were included.')),
                    h.h2(id='solution', class_='subheading')('Solution'),
                    h.img(class_='portret')(src=url_for('static', filename='covid19_1.png')),
                    h.img(class_='portret')(src=url_for('static', filename='covid19_2.png')),
                    h.img(class_='portret')(src=url_for('static', filename='covid19_3.png')),
                    h.img(class_='portret')(src=url_for('static', filename='covid19_4.png')),
                    h.img(class_='portret')(src=url_for('static', filename='covid19_5.png')),
                    h.img(class_='portret')(src=url_for('static', filename='covid19_6.png')),
                    h.img(class_='portret')(src=url_for('static', filename='covid19_7.png')),
                    h.h2(id='improvement', class_='subheading')('Space for Improvement'),
                    h.p('If I had more time:'),
                    h.ul(class_='list')(h.li('Include user testing.'),
                         h.li('Minimise text and add icons.'),
                         h.li('Add elements that would highlight the feeling of human interaction.')),
                    h.h2(id='learning', class_='subheading')('What I Learned'),
                    h.ul(class_='list')(h.li('Adjusting initial idea to the app format.'),
                         h.li('Design considerations of the project: social, behavioural, ethical.'),
                         h.li('Fast prototyping to communicate the idea.'))
                    ),
                ))
    ))
    return str(response)


@app.route('/Publication_design', methods = ['GET', 'POST'])
def Publication_design():
    '''
    Project page.
    '''
    response = h.html(h.head(
                h.link(rel="preconnect", href="https://fonts.googleapis.com"),
                h.link(rel="preconnect", href="https://fonts.gstatic.com"),
                h.link(href="https://fonts.googleapis.com/css2?family=Rubik+Dirt&family=Rubik:ital,wght@0,300..900;1,300..900&family=Titan+One&display=swap", rel="stylesheet"),
                h.link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&icon_names=emergency"),
                h.title("Anya's Portfolio"),
                h.link(rel='stylesheet', href='static/style.css')),
                h.body(class_='black')(
                    h.ul(id='navbar')(h.li(h.a('Welcome', href = '/#welcome')),
                         h.li(h.a('About me', href = '/#about')),
                         h.li(h.a('Skills', href = '/#skills')),
                         h.li(h.a('Projects', href = '/#projects')),
                         h.li(id='logo')("Anya's Portfolio")),
                    h.div(class_='container')(
                    h.div(class_='grid_menu')(
                        h.ul(h.li(h.a('Problem or Task', href = '#problem'),
                                h.li(h.a('Research', href = '#research')),
                                h.li(h.a('Solution', href = '#solution')),
                                h.li(h.a('Space for Improvement', href = '#improvement')),
                                h.li(h.a('What I Learned', href = '#learning')))),
                    ),
                    h.div(class_='grid_main')(
                    h.h1(class_='heading')('Publication Design'),
                    h.br,
                    h.div(class_='beginning')(
                    h.div(class_='for_left')(
                        h.img(class_='landscape')(src=url_for('static', filename='graphics_1.png'))),
                    h.div(class_='for_right')(
                        h.br,
                        h.h3('Time: '), h.h4('2.5 months.'),
                        h.br,
                        h.h3('Project Style: '), h.h4('individual.'),
                        h.br,
                        h.h3('Tools: '), h.h4('InDesign, Photoshop'),
                        h.br, h.h4('This publication design combines mark making, photography, manipulated images and paper collages in order to support the articles’s message with graphic language. My goal was to allow the style of the publication blend contemporary and 1930s aesthetics, to highlight the  timeless relevance of the writing.'))),
                    h.div(class_='project_description')(
                    h.h2(id='problem', class_='subheading')('Problem or Task'),
                    h.p('A publication design for “The Crystal Goblet, or Printing Should Be Invisible" by Beatrice Warde had to be from the elements created during the class, applying learnt fundamentals of typography in the layout of text and image. The mock up had to be printed in 1:1 scale.'),
                    h.h2(id='research', class_='subheading')('Research'),
                    h.p('Throughout the term, I have engaged in mark making, photography, collage making and image manipulation, learning through making. I experimented with the layout, adjusting to feedback.'),
                    h.br,
                    h.h3('1) mark making'),
                    h.img(class_='landscape')(src=url_for('static', filename='marks.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='marks_modified.png')),
                    h.h3('2) image manipulation'),
                    h.img(class_='portret')(src=url_for('static', filename='image_manipulation.JPG')),
                    h.img(class_='portret')(src=url_for('static', filename='image_manipulation_result.png')),
                    h.h3('3) collage'),
                    h.img(class_='portret')(src=url_for('static', filename='collage_1.jpg')),
                    h.img(class_='landscape')(src=url_for('static', filename='collage_2.jpg')),
                    h.h3('4) cover evolution'),
                    h.img(class_='portret')(src=url_for('static', filename='graphics_cover_1.png')),
                    h.img(class_='portret')(src=url_for('static', filename='graphics_cover_1.png')),
                    h.h3('5) breaking grid experimentation'),
                    h.img(class_='landscape')(src=url_for('static', filename='grid.png')),
                    h.h2(id='solution', class_='subheading')('Solution'),
                    h.img(class_='landscape')(src=url_for('static', filename='graphics_1.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='graphics_6.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='graphics_2.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='graphics_4.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='graphics_5.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='graphics_3.png')),
                    h.h2(id='improvement', class_='subheading')('Space for Improvement'),
                    h.p('If I had more time:'),
                    h.ul(class_='list')(h.li('Researched choice of typeface.'),
                         h.li('Photos should be taken specifically for the article, so they fit the narrative better.'),
                         h.li('Use more negative space.')),
                    h.h2(id='learning', class_='subheading')('What I Learned'),
                    h.ul(class_='list')(h.li('Layout building & visual hierarchy.'),
                         h.li('Manipulation of images’ colours.'),
                         h.li('Printing graphic design projects.'))
                    ),
                ))
    ))
    return str(response)


@app.route('/Coded_website', methods = ['GET', 'POST'])
def Coded_website():
    '''
    Project page.
    '''
    response = h.html(h.head(
                h.link(rel="preconnect", href="https://fonts.googleapis.com"),
                h.link(rel="preconnect", href="https://fonts.gstatic.com"),
                h.link(href="https://fonts.googleapis.com/css2?family=Rubik+Dirt&family=Rubik:ital,wght@0,300..900;1,300..900&family=Titan+One&display=swap", rel="stylesheet"),
                h.link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&icon_names=emergency"),
                h.title("Anya's Portfolio"),
                h.link(rel='stylesheet', href='static/style.css')),
                h.body(class_='black')(
                    h.ul(id='navbar')(h.li(h.a('Welcome', href = '/#welcome')),
                         h.li(h.a('About me', href = '/#about')),
                         h.li(h.a('Skills', href = '/#skills')),
                         h.li(h.a('Projects', href = '/#projects')),
                         h.li(id='logo')("Anya's Portfolio")),
                    h.div(class_='container')(
                    h.div(class_='grid_menu')(
                        h.ul(h.li(h.a('Problem or Task', href = '#problem'),
                                h.li(h.a('Research', href = '#research')),
                                h.li(h.a('Solution', href = '#solution')),
                                h.li(h.a('Space for Improvement', href = '#improvement')),
                                h.li(h.a('What I Learned', href = '#learning')))),
                    ),
                    h.div(class_='grid_main')(
                    h.h1(class_='heading')('Coded MyBASKET Website'),
                    h.br,
                    h.div(class_='beginning')(
                    h.div(class_='for_left')(
                        h.img(class_='landscape')(src=url_for('static', filename='coding_1.png'))),
                    h.div(class_='for_right')(
                        h.br,
                        h.h3('Time: '), h.h4('1.5 months.'),
                        h.br,
                        h.h3('Project Style: '), h.h4('individual.'),
                        h.br,
                        h.h3('Tools: '), h.h4('Figma, Visual Studio Code.'),
                        h.br, h.h4('The website fully coded by me. Using APIs, it retrieves prices from main grocery shops and analyses where your overall basket will be cheaper.'))),
                    h.div(class_='project_description')(
                    h.h2(id='problem', class_='subheading')('Problem or Task'),
                    h.p('To come up with a web solution to the chosen problem, using pyHTML and CSS coding languages.'),
                    h.h2(id='research', class_='subheading')('Research'),
                    h.h3('1) problem identification'),
                    h.br,
                    h.p("Oftentimes, grocery shops are located just a step away from each other but have different prices for the same product, meaning many people would not mind to visit both to get the best price in the current conditions of the constantly rising cost of living, if only they knew about the discounts. However it takes time to visit all different grocery shops' websites and compare the prices manually."),
                    h.br,
                    h.h3('2) target users'),
                    h.br,
                    h.p('The intended users consist of segments of the population who are trying to save money on food, live on budget and be wise with their spending, like students, low-income families or elderly people.'),
                    h.br,
                    h.h3('3) MVPs'),
                    h.br,
                    h.ul(class_='list')(h.li('Users should be able to choose several shops to include in comparison from the list.'),
                         h.li('Users should be able to type the name of the product they want to know the price for (including name, brand and size).'),
                         h.li('Website should return links for the webpages of the product on each of chosen shops website or notify if product is not found on the website (not sold in the shop).')),
                    h.br,
                    h.p('Landing page MVP: '),
                    h.img(class_='landscape')(src=url_for('static', filename='Landing page.png')),
                    h.p('Result page MVP: '),
                    h.img(class_='landscape')(src=url_for('static', filename='Result page.png')),
                    h.h3('4) "Nice to haves"'),
                    h.br,
                                        h.ul(class_='list')(h.li('Users want to remove the shop from comparison.'),
                         h.li('Users want to add another shop during the comparison.'),
                         h.li('Users want to be able to restart with a different product.'),
                         h.li('Website should be able to return the prices of the product as well as page links of it.'),
                         h.li('Not attempted: users should be able to create accounts to store their preferred shops and products.')),
                    h.br,
                    h.p('Results page with nice to haves:'),
                    h.img(class_='landscape')(src=url_for('static', filename='Result page with nice to haves.png')),
                    h.h3('5) stretch goals'),
                    h.br,
                    h.ul(class_='list')(h.li('Website can suggest product options by the first letters the user typed.'),
                         h.li('Website can count the price of the whole basket for each shop.'),
                         h.li('User should be able to compare several products from the same shops at the same time.'),
                         h.li('Not attempted: Website can accept a generic name of a product (e.g., tomatoes) and after comparing price per unit can display the cheapest option from each shop.'),
                         h.li('Not attempted: Website should be able to consider if the price is different based on the location of the shop: for example, some discounts only work for Coles in Randwick.'),
                         h.li('Not attempted: Website can compare the prices and highlight the shop with the cheapest one.')),

                    h.h2(id='solution', class_='subheading')('Solution'),
                    h.img(class_='landscape')(src=url_for('static', filename='coding_1.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='coding_2.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='coding_3.png')),
                    h.h2(id='improvement', class_='subheading')('Space for Improvement'),
                    h.p('If I had more time:'),
                    h.ul(class_='list')(h.li('Include user testing.'),
                         h.li('More engaging interface.'),
                         h.li('Ability to create accounts and save preferences with JSON files.')),
                    h.h2(id='learning', class_='subheading')('What I Learned'),
                    h.ul(class_='list')(h.li('Coding in pyHTML and CSS.'),
                         h.li('APIs.'),
                         h.li('Use of cookies.'))
                    ),
                ))
    ))
    return str(response)


@app.route('/Preservation_project', methods = ['GET', 'POST'])
def Preservation_project():
    '''
    Project page.
    '''
    response = h.html(h.head(
                h.link(rel="preconnect", href="https://fonts.googleapis.com"),
                h.link(rel="preconnect", href="https://fonts.gstatic.com"),
                h.link(href="https://fonts.googleapis.com/css2?family=Rubik+Dirt&family=Rubik:ital,wght@0,300..900;1,300..900&family=Titan+One&display=swap", rel="stylesheet"),
                h.link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&icon_names=emergency"),
                h.title("Anya's Portfolio"),
                h.link(rel='stylesheet', href='static/style.css')),
                h.body(class_='black')(
                    h.ul(id='navbar')(h.li(h.a('Welcome', href = '/#welcome')),
                         h.li(h.a('About me', href = '/#about')),
                         h.li(h.a('Skills', href = '/#skills')),
                         h.li(h.a('Projects', href = '/#projects')),
                         h.li(id='logo')("Anya's Portfolio")),
                    h.div(class_='container')(
                    h.div(class_='grid_menu')(
                        h.ul(h.li(h.a('Problem or Task', href = '#problem'),
                                h.li(h.a('Research', href = '#research')),
                                h.li(h.a('Solution', href = '#solution')),
                                h.li(h.a('Space for Improvement', href = '#improvement')),
                                h.li(h.a('What I Learned', href = '#learning')))),
                    ),
                    h.div(class_='grid_main')(
                    h.h1(class_='heading')('Preservation Project'),
                    h.br,
                    h.div(class_='beginning')(
                    h.div(class_='for_left')(
                        h.img(class_='landscape')(src=url_for('static', filename='overall.png'))),
                    h.div(class_='for_right')(
                        h.br,
                        h.h3('Time: '), h.h4('1.5 months.'),
                        h.br,
                        h.h3('Project Style: '), h.h4('individual.'),
                        h.br,
                        h.h3('Tools: '), h.h4('Blender, InDesign.'),
                        h.br, h.h4('A fully natural solution for the Southern bent-wing bat preservation. As one of their main concerns is decline in food sources, I proposed using night-blooming flowers, water sources and bug hotels to attract moths to the area and allow them to breed.'))),
                    h.div(class_='project_description')(
                    h.h2(id='problem', class_='subheading')('Problem or Task'),
                    h.p('The goal of the project is help the preservation of the Southern bent-wing bat, Australian endangered species, with a bio-inspired solution.'),
                    h.h2(id='research', class_='subheading')('Research'),
                    h.h3('1) species context: threats, locations and behaviour'),
                    h.img(class_='landscape')(src=url_for('static', filename='treats.png')),
                    h.h3('2) initial ideas'),
                    h.img(class_='landscape')(src=url_for('static', filename='initial_ideas.png')),
                    h.h3('3) idea development'),
                    h.img(class_='landscape')(src=url_for('static', filename='moodboard.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='sketch.png')),
                    h.h3('4) materials consideration'),
                    h.img(class_='landscape')(src=url_for('static', filename='materials.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='flowers.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='wayfinding_materials.png')),
                    h.h3('5) considering the system: people, bats, moths and other animals'),
                    h.img(class_='landscape')(src=url_for('static', filename='map.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='system.png')),
                    h.h3('6) positive and negative implementations'),
                    h.img(class_='landscape')(src=url_for('static', filename='implication_wheel.png')),
                    h.h2(id='solution', class_='subheading')('Solution'),
                    h.img(class_='landscape')(src=url_for('static', filename='overall.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='camera_flowers.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='bug_hotel.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='camera.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='wayfinding.png')),
                    h.img(class_='landscape')(src=url_for('static', filename='scale.png')),
                    h.h2(id='improvement', class_='subheading')('Space for Improvement'),
                    h.p('If I had more time:'),
                    h.ul(class_='list')(h.li('Create Blender elements myself and not use pre-made libraries.'),
                         h.li('Deeper analysis of materials.'),
                         h.li('More unique wayfinding system.')),
                    h.h2(id='learning', class_='subheading')('What I Learned'),
                    h.ul(class_='list')(h.li('Considerations of sustainability: lifecycle design, circular design, bio-mimicry and nature-positive design.'),
                         h.li('Interdisciplinary approach and system thinking.'),
                         h.li('Using behavioural design, persuasive design and laws of behaviour change.'))
                    ),
                ))
    ))
    return str(response)

# Start our app
if __name__ == "__main__":
    app.run(debug=True)
