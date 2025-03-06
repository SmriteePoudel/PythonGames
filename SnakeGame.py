import pygame
import sys
import random

# Constants
WIDTH, HEIGHT = 400, 600
GROUND_HEIGHT = 100
BIRD_SIZE = 40
PIPE_WIDTH = 60
PIPE_GAP = 200
GRAVITY = 0.5
FLAP_STRENGTH = 10
FORWARD_VELOCITY = 2  # Forward velocity of the bird
COUNTDOWN_TIME = 3 * 1000  # 3 seconds

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

# Initialize clock
clock = pygame.time.Clock()

# Load bird image
bird_image = pygame.image.load("bird.png")
bird_image = pygame.transform.scale(bird_image, (BIRD_SIZE, BIRD_SIZE))

# Game variables
bird_x = WIDTH // 4
bird_y = HEIGHT // 2
bird_velocity = 0
score = 0
game_over = False
countdown_start_time = pygame.time.get_ticks() + COUNTDOWN_TIME
PIPE_HEIGHT = random.randint(100, 400)  # Initial pipe height

# Initial pipe position
pipe_x = WIDTH
PIPE_HEIGHT = random.randint(100, 400)
    "import turtle\n",
    "import time\n",
    "import random\n",
    "\n",
    "delay = 0.1\n",
    "\n",
    "# Score\n",
    "score = 0\n",
    "high_score = 0\n",
    "\n",
    "# Set up the screen\n",
    "wn = turtle.Screen()\n",
    "wn.title(\"Snake Game by @TokyoEdTech\")\n",
    "wn.bgcolor(\"green\")\n",
    "wn.setup(width=600, height=600)\n",
    "wn.tracer(0) # Turns off the screen updates\n",
    "\n",
    "# Snake head\n",
    "head = turtle.Turtle()\n",
    "head.speed(0)\n",
    "head.shape(\"square\")\n",
    "head.color(\"black\")\n",
    "head.penup()\n",
    "head.goto(0,0)\n",
    "head.direction = \"stop\"\n",
    "\n",
    "# Snake food\n",
    "food = turtle.Turtle()\n",
    "food.speed(0)\n",
    "food.shape(\"circle\")\n",
    "food.color(\"red\")\n",
    "food.penup()\n",
    "food.goto(0,100)\n",
    "\n",
    "segments = []\n",
    "\n",
    "# Pen\n",
    "pen = turtle.Turtle()\n",
    "pen.speed(0)\n",
    "pen.shape(\"square\")\n",
    "pen.color(\"white\")\n",
    "pen.penup()\n",
    "pen.hideturtle()\n",
    "pen.goto(0, 260)\n",
    "pen.write(\"Score: 0  High Score: 0\", align=\"center\", font=(\"Courier\", 24, \"normal\"))\n",
    "\n",
    "# Functions\n",
    "def go_up():\n",
    "    if head.direction != \"down\":\n",
    "        head.direction = \"up\"\n",
    "\n",
    "def go_down():\n",
    "    if head.direction != \"up\":\n",
    "        head.direction = \"down\"\n",
    "\n",
    "def go_left():\n",
    "    if head.direction != \"right\":\n",
    "        head.direction = \"left\"\n",
    "\n",
    "def go_right():\n",
    "    if head.direction != \"left\":\n",
    "        head.direction = \"right\"\n",
    "\n",
    "def move():\n",
    "    if head.direction == \"up\":\n",
    "        y = head.ycor()\n",
    "        head.sety(y + 20)\n",
    "\n",
    "    if head.direction == \"down\":\n",
    "        y = head.ycor()\n",
    "        head.sety(y - 20)\n",
    "\n",
    "    if head.direction == \"left\":\n",
    "        x = head.xcor()\n",
    "        head.setx(x - 20)\n",
    "\n",
    "    if head.direction == \"right\":\n",
    "        x = head.xcor()\n",
    "        head.setx(x + 20)\n",
    "\n",
    "# Keyboard bindings\n",
    "wn.listen()\n",
    "wn.onkeypress(go_up, \"w\")\n",
    "wn.onkeypress(go_down, \"s\")\n",
    "wn.onkeypress(go_left, \"a\")\n",
    "wn.onkeypress(go_right, \"d\")\n",
    "\n",
    "# Main game loop\n",
    "while True:\n",
    "    wn.update()\n",
    "\n",
    "    # Check for a collision with the border\n",
    "    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:\n",
    "        time.sleep(1)\n",
    "        head.goto(0,0)\n",
    "        head.direction = \"stop\"\n",
    "\n",
    "        # Hide the segments\n",
    "        for segment in segments:\n",
    "            segment.goto(1000, 1000)\n",
    "        \n",
    "        # Clear the segments list\n",
    "        segments.clear()\n",
    "\n",
    "        # Reset the score\n",
    "        score = 0\n",
    "\n",
    "        # Reset the delay\n",
    "        delay = 0.1\n",
    "\n",
    "        pen.clear()\n",
    "        pen.write(\"Score: {}  High Score: {}\".format(score, high_score), align=\"center\", font=(\"Courier\", 24, \"normal\")) \n",
    "\n",
    "\n",
    "    # Check for a collision with the food\n",
    "    if head.distance(food) < 20:\n",
    "        # Move the food to a random spot\n",
    "        x = random.randint(-290, 290)\n",
    "        y = random.randint(-290, 290)\n",
    "        food.goto(x,y)\n",
    "\n",
    "        # Add a segment\n",
    "        new_segment = turtle.Turtle()\n",
    "        new_segment.speed(0)\n",
    "        new_segment.shape(\"square\")\n",
    "        new_segment.color(\"grey\")\n",
    "        new_segment.penup()\n",
    "        segments.append(new_segment)\n",
    "\n",
    "        # Shorten the delay\n",
    "        delay -= 0.001\n",
    "\n",
    "        # Increase the score\n",
    "        score += 10\n",
    "\n",
    "        if score > high_score:\n",
    "            high_score = score\n",
    "        \n",
    "        pen.clear()\n",
    "        pen.write(\"Score: {}  High Score: {}\".format(score, high_score), align=\"center\", font=(\"Courier\", 24, \"normal\")) \n",
    "\n",
    "    # Move the end segments first in reverse order\n",
    "    for index in range(len(segments)-1, 0, -1):\n",
    "        x = segments[index-1].xcor()\n",
    "        y = segments[index-1].ycor()\n",
    "        segments[index].goto(x, y)\n",
    "\n",
    "    # Move segment 0 to where the head is\n",
    "    if len(segments) > 0:\n",
    "        x = head.xcor()\n",
    "        y = head.ycor()\n",
    "        segments[0].goto(x,y)\n",
    "\n",
    "    move()    \n",
    "\n",
    "    # Check for head collision with the body segments\n",
    "    for segment in segments:\n",
    "        if segment.distance(head) < 20:\n",
    "            time.sleep(1)\n",
    "            head.goto(0,0)\n",
    "            head.direction = \"stop\"\n",
    "        \n",
    "            # Hide the segments\n",
    "            for segment in segments:\n",
    "                segment.goto(1000, 1000)\n",
    "        \n",
    "            # Clear the segments list\n",
    "            segments.clear()\n",
    "\n",
    "            # Reset the score\n",
    "            score = 0\n",
    "\n",
    "            # Reset the delay\n",
    "            delay = 0.1\n",
    "        \n",
    "            # Update the score display\n",
    "            pen.clear()\n",
    "            pen.write(\"Score: {}  High Score: {}\".format(score, high_score), align=\"center\", font=(\"Courier\", 24, \"normal\"))\n",
    "\n",
    "    time.sleep(delay)\n",
    "\n",
    "wn.mainloop()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a5958fc-32cc-4aec-8fdf-3d9018bdfd16",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:anaconda3]",
   "language": "python",
   "name": "conda-env-anaconda3-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
