import pygame, sys
from pygame.locals import QUIT
from character import Character
pygame.init()
timer = pygame.time.get_ticks()
level = 1
positionX = 275
positionY = 750
character = Character((positionX, positionY))
speedX = 0
character.speedY = 1
gravity = 0.075
Speed1 = 0.75
SuperFastSpeed = False
SuperHighJump = False
SuperSlowSpeed = False
UnmovingSpeed = False
cash = 10000
AvailableJumps = 1
ShowUI = True
xValue1 = 400
yValue1 = 400
JumpJumpJumpJump = AvailableJumps
SpeedSpeedSpeedSpeed = (0, 255, 0)
SpeedSpeedSpeed = "Slow"
SpeedSpeed = 0.05
SpeedColor = (0, 255, 0)
JumpColor = (0, 255, 0)
JumpPower = 7.5
DeathSpeed = 800
PlatformColor = 12
PlatformText = (0, 0, 0)
CharacterColor = 7
CharacterText = (0, 0, 0)
BackgroundColor = 6
BackgroundText = (0, 0, 0)
BackgroundColors = {
  1:["Red", (255, 0, 0)],
  2:["Orange", (255, 165, 0)],
  3:["Yellow", (255, 255, 0)],
  4:["Green", (0, 255, 0)],
  5:["Dark Green", (0, 175, 0)],
  6:["Teal", (0, 255, 255)],
  7:["Blue", (0, 0, 255)],
  8:["Purple", (190, 0, 190)],
  9:["Pink", (255, 0, 255)],
  10:["White", (255, 255, 255)],
  11:["Gray", (100, 100, 100)],
  12:["Black", (0, 0, 0)]}
DeathColor = 1
DeathText = (0, 0, 0)
DeathTypes = {
  1:["Lava", (255, 0, 0)],
  2:["Fire", (255, 165, 0)],
  3:["Electricity", (255, 255, 0)],
  4:["Poison", (0, 255, 0)], 
  5:["Ice", (0, 255, 255)],
  6:["Ocean", (0, 0, 255)],
  7:["Empty Space", (255, 255, 255)],
  8:["Mountains", (100, 100, 100)],
  9:["Bottomless Pit", (0, 0, 0)]}
Themes1 = {
  1:["Hacker", 4, 12, 4, 4],
  2:["Scary", 1, 12, 1, 1],
  3:["Old School", 12, 10, 12, 9],
  4:["Reversed", 10, 12, 10, 7], 
  5:["Christmas", 4, 6, 1, 7],
  6:["Halloween", 1, 12, 2, 2]
}
Themes2 = {
  1:["Nature", 11, 4, 11, 8],
  2:["Sea", 7, 6, 11, 6],
  3:["Spring", 4, 3, 9, 4],
  4:["Summer", 2, 6, 4, 3],
  5:["Fall", 1, 2, 11, 3],
  6:["Winter", 6, 10, 11, 5]
}
Items = {
  "Super Fast Speed": [Speed1, 1, 100],
  "Super High Jump": [JumpPower, 500, 100],
  "Double Jump": [AvailableJumps, 2, 250],
  "Super Slow": [SuperSlowSpeed, 100],
  "Unmoving": [UnmovingSpeed, 500]
}
SpeedMode = "Speed: Fast"
JumpMode = "Jump Height: High"
font = pygame.font.SysFont("Arial", 20, bold = True)
display = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Python Games")
def drawplatform(Color, Location, character, AvailableJumps):
          x = Location[0]
          y = Location[1]
          width = Location[2]
          pygame.draw.rect(display, Color, Location)
          if character.position[0] > x - 100 and character.position[0] < x + width and character.position[1] > y and character.position[1] < y + 20:
            character.move(0, -character.speedY)
            character.speedY = 0
            AvailableJumps = JumpJumpJumpJump
          return AvailableJumps
while True:
    UIToggle = pygame.Rect(1475, 125, 150, 75)
    LevelDisplay = font.render("Level: " + str(level), True, (0, 0, 0))
    Cash = font.render("Cash: " + str(cash), True, (0, 0, 0))
    Speed = font.render(SpeedMode, True, (0, 0, 0))
    Jump = font.render(JumpMode, True, (0, 0, 0))
    Color = font.render("Character Color: " + BackgroundColors[CharacterColor][0], True, CharacterText)
    Color2 = font.render("Background Color: " + BackgroundColors[BackgroundColor][0], True, BackgroundText)
    Color3 = font.render("Platform Color: " + BackgroundColors[PlatformColor][0], True, PlatformText)
    Death = font.render("Death Type: " + DeathTypes[DeathColor][0], True, DeathText)
    Death2 = font.render(DeathTypes[DeathColor][0] + " Speed: " + str(SpeedSpeedSpeed), True, (0, 0, 0))
    HowToToggleUI = font.render("Type \"C\" to close UI & type \"O\" to open UI", True, (0, 0, 0))
    ResetSettings = font.render("Reset Settings", True, (0, 0, 0))
    display.fill(BackgroundColors[BackgroundColor][1])
    if BackgroundColor == 12:
      BackgroundText = (255, 255, 255)
    else:
      BackgroundText = (0, 0, 0)  
    if CharacterColor == 12:
      CharacterText = (255, 255, 255)
    else:
      CharacterText = (0, 0, 0)
    if PlatformColor == 12:
      PlatformText = (255, 255, 255)
    else:
      PlatformText = (0, 0, 0)
    if DeathColor == 9:
       DeathText = (255, 255, 255)
    else:
      DeathText = (0, 0, 0)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_a:
            speedX = -Speed1
          if event.key == pygame.K_d:
            speedX = Speed1
          if event.key == pygame.K_w and AvailableJumps > 0:
            character.speedY = -JumpPower
            AvailableJumps -= 1
          if event.key == pygame.K_c:
            ShowUI = False
          if event.key == pygame.K_o:
            ShowUI = True
        if event.type == pygame.KEYUP:
          if event.key == pygame.K_a:
            speedX = 0
          if event.key == pygame.K_d:
            speedX = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
          mousex, mousey = pygame.mouse.get_pos()
          if ShowUI:
            if mousex > 190 and mousex < 370 and mousey > 195 and mousey < 230:
                if SuperFastSpeed == True and SpeedMode == "Speed: Fast":
                  SpeedMode = "Speed: Super Fast"
                  Speed1 = 1 
                  SpeedColor = (190, 0, 190)
                elif SpeedMode == "Speed: Super Fast":
                  SpeedMode = "Speed: Slow"
                  Speed1 = 0.25
                  SpeedColor = (255, 0, 0)
                elif SpeedMode == "Speed: Fast":
                  SpeedMode = "Speed: Slow"
                  Speed1 = 0.25
                  SpeedColor = (255, 0, 0)
                elif SpeedMode == "Speed: Slow":
                  SpeedMode = "Speed: Medium"
                  Speed1 = 0.5
                  SpeedColor = (255, 255, 0)
                else:
                  SpeedMode = "Speed: Fast"
                  Speed1 = 0.75
                  SpeedColor = (0, 255, 0)
            elif mousex > 190 and mousex < 435 and mousey > 235 and mousey < 270:
                if SuperHighJump == True and JumpMode == "Jump Height: High":
                  JumpMode = "Jump Height: Super High"
                  JumpPower = 10
                  JumpColor = (190, 0, 190)
                elif JumpMode == "Jump Height: Super High":
                  JumpMode = "Jump Height: Low"
                  JumpPower = 2.5
                  JumpColor = (255, 0, 0)
                elif JumpMode == "Jump Height: High":
                  JumpMode = "Jump Height: Low"
                  JumpPower = 2.5
                  JumpColor = (255, 0, 0)
                elif JumpMode == "Jump Height: Low":
                  JumpMode = "Jump Height: Medium"
                  JumpPower = 5
                  JumpColor = (255, 255, 0)
                else:
                  JumpMode = "Jump Height: High"
                  JumpPower = 7.5
                  JumpColor = (0, 255, 0)
            elif mousex > 190 and mousex < 430 and mousey > 275 and mousey < 310:
              if CharacterColor < 12:
                CharacterColor += 1
              else:
                CharacterColor = 1
            elif mousex > 190 and mousex < 445 and mousey > 315 and mousey < 350:
              if BackgroundColor < 12:
                BackgroundColor += 1
              else:
                BackgroundColor = 1
            elif mousex > 190 and mousex < 445 and mousey > 355 and mousey < 390:
              if PlatformColor < 12:
                PlatformColor += 1
              else:
                PlatformColor = 1
            elif mousex > 190 and mousex < 445 and mousey > 395 and mousey < 430:
              if DeathColor < 9:
                DeathColor += 1
              else:
                DeathColor = 1
            elif mousex > 190 and mousex < 480 and mousey > 435 and mousey < 470:
                if UnmovingSpeed == True and SpeedSpeedSpeed == "Fast":
                  SpeedSpeedSpeed = "Unmoving"
                  SpeedSpeed = 0
                  SpeedSpeedSpeedSpeed = (0, 0, 255)
                elif UnmovingSpeed == True and SuperSlowSpeed == True and SpeedSpeedSpeed == "Unmoving":
                  SpeedSpeedSpeed = "Super Slow"
                  SpeedSpeed = 0.025
                  SpeedSpeedSpeedSpeed = (190, 0, 190)
                elif UnmovingSpeed == True and SuperSlowSpeed == False and SpeedSpeedSpeed == "Unmoving":
                  SpeedSpeedSpeed = "Slow"
                  SpeedSpeed = 0.05
                  SpeedSpeedSpeedSpeed = (0, 255, 0)
                elif SuperSlowSpeed == True and UnmovingSpeed == False and SpeedSpeedSpeed == "Fast":
                  SpeedSpeedSpeed = "Super Slow"
                  SpeedSpeed = 0.025
                  SpeedSpeedSpeedSpeed = (190, 0, 190)
                elif SpeedSpeedSpeed == "Super Slow":
                  SpeedSpeedSpeed = "Slow"
                  SpeedSpeed = 0.05
                  SpeedSpeedSpeedSpeed = (0, 255, 0)
                elif SpeedSpeedSpeed == "Fast":
                  SpeedSpeedSpeed = "Slow"
                  SpeedSpeed = 0.05
                  SpeedSpeedSpeedSpeed = (0, 255, 0)
                elif SpeedSpeedSpeed == "Slow":
                  SpeedSpeedSpeed = "Medium"
                  SpeedSpeed = 0.1
                  SpeedSpeedSpeedSpeed = (255, 255, 0)
                else:
                  SpeedSpeedSpeed = "Fast"
                  SpeedSpeed = 0.2
                  SpeedSpeedSpeedSpeed = (255, 0, 0)
            elif mousex > 495 and mousex < 870 and mousey > 115 and mousey < 320:
              itemposition = 115
              for k, v in Items.items():
                if mousex > 500 and mousex < 875 and mousey > itemposition and mousey < itemposition + 35:
                  if v[-1] <= cash:
                    cash -= v[-1]
                    v[-1] = 0
                    if k == "Super Fast Speed":
                      SuperFastSpeed = True
                    elif k == "Super High Jump":
                      SuperHighJump = True
                    elif k == "Double Jump":
                      AvailableJumps = 2
                      JumpJumpJumpJump = AvailableJumps
                    elif k == "Unmoving":
                      UnmovingSpeed = True
                    else:
                      SuperSlowSpeed = True
                itemposition += 40
            elif mousex > 505 and mousex < 630 and mousey > 330 and mousey < 465:
               Speed1 = 0.75
               SpeedMode = "Speed: Fast"
               SpeedColor = (0, 255, 0)
               JumpMode = "Jump Height: High"
               JumpPower = 7.5
               JumpColor = (0, 255, 0)
               CharacterColor = 7
               BackgroundColor = 6
               PlatformColor = 12
               DeathColor = 1
               SpeedSpeed = 0.05
               SpeedSpeedSpeed = "Slow"
               SpeedSpeedSpeedSpeed = (0, 255, 0)
            elif mousex > 880 and mousex < 1255 and mousey > 115 and mousey < 645:
              itemposition = 115
              for k, v in Themes1.items():
                if mousex > 885 and mousex < 1050 and mousey > itemposition and mousey < itemposition + 35:
                   CharacterColor = v[1]
                   BackgroundColor = v[2]
                   PlatformColor = v[3]
                   DeathColor = v[4]
                itemposition += 40
              itemposition = 115
              for k, v in Themes2.items():
                if mousex > 1055 and mousex < 1210 and mousey > itemposition and mousey < itemposition + 35:
                   CharacterColor = v[1]
                   BackgroundColor = v[2]
                   PlatformColor = v[3]
                   DeathColor = v[4]
                itemposition += 40
    character.move(speedX, character.speedY)
    character.speedY += gravity
    oldpositionY = character.position[1]
    oldAvailableJumps = AvailableJumps
    if level == 1:
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (250, 750, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (420, 700, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (590, 650, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (760, 600, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (930, 550, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (1100, 500, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (1270, 450, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (1440, 400, 150, 20), character, AvailableJumps)
    elif level == 2:
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (250, 750, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (420, 600, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (590, 700, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (760, 550, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (930, 650, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (1100, 500, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (1270, 600, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (1440, 450, 150, 20), character, AvailableJumps)
    elif level == 3:
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (250, 750, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (500, 700, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (750, 650, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (1000, 600, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (1250, 600, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (1300, 450, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (1350, 300, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (1400, 150, 150, 20), character, AvailableJumps)
    elif level == 4:
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (250, 750, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (300, 600, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (250, 450, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (300, 300, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (250, 150, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (650, 350, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (800, 450, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (950, 350, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (1300, 450, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (1300, 300, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (1300, 150, 150, 20), character, AvailableJumps)
    elif level == 5:
          if xValue1 >= 750:
             SpeedPlatform = -0.5
          elif xValue1 <= 400:
             SpeedPlatform = 0.5
          if character.position[0] >= xValue1 - 100 and character.position[0] <= xValue1 + 150 and character.position[1] >= 745 and character.position[1] <= 755:
             character.position[0] += SpeedPlatform
          xValue1 += SpeedPlatform
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (xValue1, 750, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (250, 750, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (1000, 600, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (1150, 450, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (1300, 300, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (1450, 150, 150, 20), character, AvailableJumps)
    elif level == 6:
          if yValue1 >= 750:
            SpeedPlatform2 = -0.5
          elif yValue1 <= 400:
            SpeedPlatform2 = 0.5
          if character.position[0] >= 300 and character.position[0] <= 550 and character.position[1] >= yValue1 - 5 and character.position[1] <= yValue1 + 5:
             character.position[1] += SpeedPlatform2
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (400, yValue1, 150, 20), character, AvailableJumps)
          AvailableJumps = drawplatform(BackgroundColors[PlatformColor][1], (250, 750, 150, 20), character, AvailableJumps)
          yValue1 += SpeedPlatform2
    if oldpositionY == character.position[1] and oldAvailableJumps == AvailableJumps:
      jump = False
    DeathThing = pygame.draw.rect(display, DeathTypes[DeathColor][1], (0, DeathSpeed, 2000, 1000))
    DeathSpeed -= SpeedSpeed
    if ShowUI:
      Settings = pygame.draw.rect(display, (175, 175, 200), (190, 100, 300, 380))
      Settings2 = pygame.draw.rect(display, (175, 175, 200), (500, 330, 375, 135))
      Shop = pygame.draw.rect(display, (175, 175, 200), (500, 100, 375, 220))
      Theme = pygame.draw.rect(display, (175, 175, 200), (885, 100, 340, 260))
      itemposition = 115
      for k, v in Items.items():
        if k != "Unmoving" and k != "Super Slow": 
          pygame.draw.rect(display, (190, 0, 190), (505, itemposition, 365, 35))
          ItemText = font.render(k + ": " + str(v[-1]) + " Cash", True, (0, 0, 0))
          if v[-1] == 0:
            ItemText = font.render(k + ": Purchased", True, (0, 0, 0))
          display.blit(ItemText, (510, itemposition + 5))
          itemposition += 40
      pygame.draw.rect(display, (190, 0, 190), (505, itemposition, 365, 35))
      if SuperSlowSpeed == False:
         ItemText = font.render("Super Slow " + DeathTypes[DeathColor][0] + " Speed" + ": 100 Cash", True, (0, 0, 0))
      else:
         ItemText = font.render("Super Slow " + DeathTypes[DeathColor][0] + " Speed" + ": Purchased", True, (0, 0, 0))
      display.blit(ItemText, (510, itemposition + 5))
      itemposition += 40
      pygame.draw.rect(display, (190, 0, 190), (505, itemposition, 365, 35))
      if UnmovingSpeed == False:
         ItemText = font.render("Unmoving " + DeathTypes[DeathColor][0] + " Speed" + ": 500 Cash", True, (0, 0, 0))
      else:
         ItemText = font.render("Unmoving " + DeathTypes[DeathColor][0] + " Speed" + ": Purchased", True, (0, 0, 0))
      display.blit(ItemText, (510, itemposition + 5))
      itemposition = 115
      for k, v in Themes1.items():
          pygame.draw.rect(display, BackgroundColors[v[2]][1], (890, itemposition, 160, 35))
          ItemText = font.render(v[0] + " Theme", True, BackgroundColors[v[1]][1])
          display.blit(ItemText, (895, itemposition + 5))
          itemposition += 40
      itemposition = 115
      for k, v in Themes2.items():
          pygame.draw.rect(display, BackgroundColors[v[2]][1], (1055, itemposition, 160, 35))
          ItemText = font.render(v[0] + " Theme", True, BackgroundColors[v[1]][1])
          display.blit(ItemText, (1060, itemposition + 5))
          itemposition += 40
      LevelSettings = pygame.draw.rect(display, (255, 255, 255), (195, 115, 100, 35))
      CashSettings = pygame.draw.rect(display, (255, 255, 0), (195, 155, 100, 35))  
      SpeedSettings = pygame.draw.rect(display, SpeedColor, (195, 195, 175, 35))
      JumpSettings = pygame.draw.rect(display, JumpColor, (195, 235, 240, 35))
      CharacterSettings = pygame.draw.rect(display, BackgroundColors[CharacterColor][1], (195, 275, 235, 35))
      BackgroundSettings = pygame.draw.rect(display, BackgroundColors[BackgroundColor][1], (195, 315, 250, 35))
      PlatformSettings = pygame.draw.rect(display, BackgroundColors[PlatformColor][1], (195, 355, 250, 35))
      DeathSettings = pygame.draw.rect(display, DeathTypes[DeathColor][1], (195, 395, 250, 35))
      Death2Settings = pygame.draw.rect(display, SpeedSpeedSpeedSpeed, (195, 435, 285, 35))
      HowToTogggleUISettings = pygame.draw.rect(display, (0, 255, 0), (505, 340, 360, 35))
      ResetSettingsSettings = pygame.draw.rect(display, (255, 0, 0), (505, 420, 125, 35))
      display.blit(LevelDisplay, (200, 120))
      display.blit(Cash, (200, 160))
      display.blit(Speed, (200, 200))
      display.blit(Jump, (200, 240))
      display.blit(Color, (200, 280))
      display.blit(Color2, (200, 320))
      display.blit(Color3, (200, 360))
      display.blit(Death, (200, 400))
      display.blit(Death2, (200, 440))
      display.blit(HowToToggleUI, (510, 345))
      display.blit(ResetSettings, (510, 425))
    player = pygame.draw.polygon(display, 
BackgroundColors[CharacterColor][1], ((character.position[0] + 50, character.position[1] - 75), (character.position[0], character.position[1]), (character.position[0] + 100, character.position[1])))
    drawplatform((255, 215, 0), (1650, 100, 150, 900), character, AvailableJumps)
    if character.position[0] > 1550:
      cash += level * 10
      level += 1
      DeathSpeed = 800
      character.speedY = 0
      character.setposition(275, 750)
    if character.position[1] > DeathSpeed:
      character.setposition(275, 750)
      DeathSpeed = 800
      character.speedY = 0
    pygame.display.update()