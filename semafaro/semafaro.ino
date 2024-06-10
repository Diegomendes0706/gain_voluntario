const int ledVermelho = 35;
const int ledAmarelo = 33;
const int ledVerde = 26;
const int botao = 34;
const int LEDs[3] = {ledVermelho, ledAmarelo, ledVerde};
int estadoBotao ;

void setup() {
  pinMode(botao, INPUT);
  pinMode(ledAmarelo, OUTPUT);
  pinMode(ledVermelho, OUTPUT);
  pinMode(ledVerde, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  estadoBotao = digitalRead(botao);
  if (estadoBotao == HIGH){
    for (int i = 0; i < 3; i++){
      digitalWrite(LEDs[i], HIGH);
      if (i == 2){
        delay(500);
      }
      else{
        delay(1000);
      }
      digitalWrite(LEDs[i], LOW);
    }
  Serial.println(estadoBotao);
  delay(100);
  }
  estadoBotao = digitalRead(botao);
}
