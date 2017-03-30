// Two pin motor driver example, from RoboPi User Manual, p.24&25
//

// http://www.mikronauts.com/wp-content/upload/2014/01/RoboPi-User-Manual-v0.85b.pdf
//

// William Henning, Mikronauts


#include <stdio.h>

#include "RoboPiLib.h"


#define MOTORA_IA       12

#define MOTORA_IB       13

#define MOTORB_IA       14

#define MOTORB_IB       15


int main(int argc, char *argv[])
 {

   int i;

   RoboPiInit("/dev/ttyAMA0",115200);

   while(1) {

      // set both motors FORWARD

      pinMode(MOTORA_IA,PWM);

      pinMode(MOTORA_IB,OUTPUT);

      digitalWrite(MOTORA_IB,0);

      pinMode(MOTORB_IA,PWM);

      pinMode(MOTORB_IB,OUTPUT);

      digitalWrite(MOTORB_IB,0);

      for(i=0;i<256;i+=16) {

         analogWrite(MOTORA_IA, i);

         analogWrite(MOTORB_IA, i);

         sleep(1);
      }


      for(i=255;i>0;i-=16) {

         analogWrite(MOTORA_IA, i);

         analogWrite(MOTORB_IA, i);

         sleep(1);
      }

      // set both motors REVERSE

      pinMode(MOTORA_IA,OUTPUT);

      digitalWrite(MOTORA_IA,0);

      pinMode(MOTORA_IB,PWM);

      pinMode(MOTORB_IA,OUTPUT);

      digitalWrite(MOTORB_IA,0);

      pinMode(MOTORB_IB,PWM);

      for(i=0;i<256;i+=16) {

         analogWrite(MOTORA_IB, i);

         analogWrite(MOTORB_IB, i);

         sleep(1);

      }

      for(i=255;i>0;i-=16) {

         analogWrite(MOTORA_IB, i);

         analogWrite(MOTORB_IB, i);

         sleep(1);

      }

   }

 }
