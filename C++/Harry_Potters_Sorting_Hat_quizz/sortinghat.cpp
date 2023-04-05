#include <iostream>
 
int main() {
 
  // The magic starts here
  int gryffindor = 0, hufflepuff = 0, ravenclaw = 0, slytherin = 0;

  int answer1, answer2, answer3, answer4;

  std::cout << "=====================\n";
  std::cout << "The Sorting Hat Quiz!\n";
  std::cout << "=====================\n\n";

  std::cout << "Q1) When I'm dead, I want people to remember me as:\n\n";
 
  std::cout << "  1) The Good\n";
  std::cout << "  2) The Great\n";
  std::cout << "  3) The Wise\n";
  std::cout << "  4) The Bold\n\n";

std::cin >> answer1;

if(answer1 == 1){
  hufflepuff++;
}
else if(answer1 == 2){
  slytherin++;
}
else if(answer1 == 3){
  ravenclaw++;
}
else if(answer1 == 4){
  gryffindor++;
}
else{
  std::cout << "Invalid input.\n";
}
  std::cout << "Q2) Dawn or Dusk?\n\n";
 
  std::cout << "  1) Dawn\n";
  std::cout << "  2) Dusk\n";

  std::cin >> answer2;

  if(answer2 == 1){
    gryffindor++;
    ravenclaw++;
  }
  else if(answer2 == 2){
    hufflepuff++;
    slytherin++;
  }
  else{
    std::cout<<"Invalid input\n";
  }

  std::cout << "Q3) Which kind of instrument most pleases your ear?\n\n";
 
  std::cout << "  1) The violin\n";
  std::cout << "  2) The trumpet\n";
  std::cout << "  3) The piano\n";
  std::cout << "  4) The drum\n\n";

  std::cin >> answer3;

  if(answer3 == 1){
    slytherin++;
  }
  else if(answer3 == 2){
    hufflepuff++;
  }
  else if(answer3 == 3){
    ravenclaw++;
  }
  else if(answer3 == 4){
    gryffindor++;
  }
  else{
    std::cout << "Invalid input.\n";
  }

  std::cout << "Q4) Which road tempts you most?\n\n";
 
  std::cout << "  1) The wide, sunny grassy lane\n";
  std::cout << "  2) The narrow, dark, lantern-lit alley\n";
  std::cout << "  3) The twisting, leaf-strewn path through woods\n";
  std::cout << "  4) The cobbled street lined (ancient buildings)\n\n";

  std::cin >> answer3;

  if(answer3 == 1){
    hufflepuff++;
  }
  else if(answer3 == 2){
    slytherin++;
  }
  else if(answer3 == 3){
    gryffindor++;
  }
  else if(answer3 == 4){
    ravenclaw++;
  }
  else{
    std::cout << "Invalid input.\n";
  }

  int max;
  std::string house;

  if (gryffindor > max) {
 
  max = gryffindor;
  house = "Gryffindor";
 
}
 
if (hufflepuff > max) {
 
  max = hufflepuff;
  house = "Hufflepuff";
 
}
 
if (ravenclaw > max) {
 
  max = ravenclaw;
  house = "Ravenclaw";
 
}
 
if (slytherin > max) {
 
  max = slytherin;
  house = "Slytherin";
 
}
 
std::cout << house << "!\n";
} 