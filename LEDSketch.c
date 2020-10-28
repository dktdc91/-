//PINの定義
const int RED_PIN = 13;
const int YELLOW_PIN = 12;
const int GREEN_PIN = 11;

const int BAUD_RATE = 9600;

//bit定義
const int RED = 0b000001;
const int YELLOW = 0b000010;
const int GREEN = 0b000100;

//loop変数
char incomingOption;
int option;
int range;

void setup() {
  pinMode(RED_PIN, OUTPUT);
  pinMode(GREEN_PIN, OUTPUT);
  pinMode(YELLOW_PIN, OUTPUT);

  Serial.begin(BAUD_RATE);
}

void loop() {
  incomingOption = Serial.read();     //シリアルI/Fからの通信を読む
  option = incomingOption - '0';      //char -> int変換
  if(option >= 0 && option <= 7){     //optionの範囲確認
    range = option;                   //LED点灯状態を設定
 
    if((range & RED) == RED){         //REDビットが立ち
      digitalWrite(RED_PIN, HIGH);
    }else{
      digitalWrite(RED_PIN, LOW);
    }
  
    if((range & GREEN) == GREEN){     //GREENビットが立ち
      digitalWrite(GREEN_PIN, HIGH);
    }else{
      digitalWrite(GREEN_PIN, LOW);
    }
  
    if((range & YELLOW) == YELLOW){   //YELLOWビットが立ち
      digitalWrite(YELLOW_PIN, HIGH);
    }else{
      digitalWrite(YELLOW_PIN, LOW);
    }
    
  }
  
}
