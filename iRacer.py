#!/usr/bin/python
#https://nebelprog.wordpress.com/2013/09/02/create-a-simple-game-menu-with-pygame-pt-4-connecting-it-to-functions/
 
import sys
import pygame
import os
import modules.configuration.active_settings as st
from shutil import copyfile
import modules.bluetooth_controls.connection as bt
import modules.interface.keyboard_input as key

pygame.init()
 
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
 
class MenuItem(pygame.font.Font):
    def __init__(self, text, font=None, font_size=30,
                 font_color=WHITE, (pos_x, pos_y)=(0, 0)):
 
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y
 
    def is_mouse_selection(self, (posx, posy)):
        if (posx >= self.pos_x and posx <= self.pos_x + self.width) and \
            (posy >= self.pos_y and posy <= self.pos_y + self.height):
                return True
        return False
 
    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y
 
    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)
 
class GameMenu():
    def __init__(self, screen, items, funcs, bg_color=BLACK, font=None, font_size=30,
                 font_color=WHITE):
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
 
        self.bg_color = bg_color
        self.clock = pygame.time.Clock()
 
        self.funcs = funcs
        self.items = []
        for index, item in enumerate(items):
            menu_item = MenuItem(item, font, font_size, font_color)
 
            # t_h: total height of text block
            t_h = len(items) * menu_item.height
            pos_x = (self.scr_width / 2) - (menu_item.width / 2)
            # This line includes a bug fix by Ariel (Thanks!)
            # Please check the comments section of pt. 2 for an explanation
            pos_y = (self.scr_height/2) - (t_h/2) + ((index*2) + index * menu_item.height)
            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)
 
        self.mouse_is_visible = True
        self.cur_item = None
 
    def set_mouse_visibility(self):
        if self.mouse_is_visible:
            pygame.mouse.set_visible(True)
        else:
            pygame.mouse.set_visible(False)
 
    def set_keyboard_selection(self, key):
        """
        Marks the MenuItem chosen via up and down keys.
        """
        for item in self.items:
            # Return all to neutral
            item.set_italic(False)
            item.set_font_color(WHITE)
 
        if self.cur_item is None:
            self.cur_item = 0
        else:
            # Find the chosen item
            if key == pygame.K_UP and \
                    self.cur_item > 0:
                self.cur_item -= 1
            elif key == pygame.K_UP and \
                    self.cur_item == 0:
                self.cur_item = len(self.items) - 1
            elif key == pygame.K_DOWN and \
                    self.cur_item < len(self.items) - 1:
                self.cur_item += 1
            elif key == pygame.K_DOWN and \
                    self.cur_item == len(self.items) - 1:
                self.cur_item = 0
 
        self.items[self.cur_item].set_italic(True)
        self.items[self.cur_item].set_font_color(RED)
 
        # Finally check if Enter or Space is pressed
        if key == pygame.K_SPACE or key == pygame.K_RETURN:
            text = self.items[self.cur_item].text
            self.funcs[text]()
 
    def set_mouse_selection(self, item, mpos):
        """Marks the MenuItem the mouse cursor hovers on."""
        if item.is_mouse_selection(mpos):
            item.set_font_color(RED)
            item.set_italic(True)
        else:
            item.set_font_color(WHITE)
            item.set_italic(False)
 
    def run(self):
        mainloop = True
        while mainloop:
            # Limit frame speed to 50 FPS
            self.clock.tick(50)
 
            mpos = pygame.mouse.get_pos()
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    mainloop = False
                if event.type == pygame.KEYDOWN:
                    self.mouse_is_visible = False
                    self.set_keyboard_selection(event.key)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for item in self.items:
                        if item.is_mouse_selection(mpos):
                            self.funcs[item.text]()
 
            if pygame.mouse.get_rel() != (0, 0):
                self.mouse_is_visible = True
                self.cur_item = None
 
            self.set_mouse_visibility()
 
            # Redraw the background
            self.screen.fill(self.bg_color)
 
            for item in self.items:
                if self.mouse_is_visible:
                    self.set_mouse_selection(item, mpos)
                self.screen.blit(item.label, item.position)
 
            pygame.display.flip()
 
if __name__ == "__main__":
    def main_menu():
        menu_items = ('Start', 'Settings', 'Quit')
        funcs = {'Start': start,
                 'Settings': settings,
                 'Quit': quit_app}

        pygame.display.set_caption('iRacer: Main Menu')
        # gm = GameMenu(screen,funcs.keys(), funcs) # gives wrong order from function keys
        gm = GameMenu(screen, menu_items, funcs)
        gm.run()

    def start():
        menu_items = ('Connect', 'Disconnect', 'Control', 'Back')
        funcs = {'Connect': connect,
                 'Disconnect': disconnect,
                 'Control': control,
                 'Back': main_menu}

        pygame.display.set_caption('iRacer: Start')
        # gm = GameMenu(screen,funcs.keys(), funcs) # gives wrong order from function keys
        gm = GameMenu(screen, menu_items, funcs)
        gm.run()

    connected = False
    def connect():
        global connected
        try:
            #print ("trying to connect")
            st.load_config()
            #print ("loading config")
            bt.initialise_bluetooth_settings()
            #print ("initialise bluetooth")
            bt.connect_bluetooth()
            #print ("connecting")
            connected = True
        except:
            connected =  False

    def disconnect():
        global connected
        if connected:
            try:
                bt.disconnect_bluetooth()
                connected = False
            except:
                connected = True
        else:
            pass



    def control():
        if connected:
            key.check_active_keys()
        else:
            pass
    def quit_app():
        disconnect()
        sys.exit()

    def settings():
        menu_items = ('Open Settings File', 'Restore Default Settings', 'Back')
        funcs = {'Open Settings File': open_settings,
                 'Restore Default Settings': restore_def_settings,
                 'Back': main_menu}
        pygame.display.set_caption('iRacer: Settings')
        gm = GameMenu(screen, menu_items, funcs)
        gm.run()

    def open_settings():
        #Instead of opening settings figure out how to do following...get settings menu from QT - and start it from different file
        #before doing anything
        print ("opening settings")
        if "linux" in sys.platform:
            print "Inside Linux open editor"
        elif "win" in sys.platform:
            print "Inside Windows open editor"
            os.system(st.correctPath[0])

    def restore_def_settings():
        print ("restoring default settings")
        copyfile('modules/configuration/config_default.ini','modules/configuration/config.ini')
 
    # Creating the screen
    screen = pygame.display.set_mode((350, 240), 0, 32)
    main_menu()
