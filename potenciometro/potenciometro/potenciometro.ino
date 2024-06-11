#define pinoSensor 2
int valorSensor = 0;
float voltagem, porcentagem;

void setup() {
  Serial.begin(9600);
  delay(100);
}

void loop() {
  valorSensor = analogRead(pinoSensor);
  voltagem = valorSensor * (3.3/4098);
  porcentagem = (valorSensor * 100)/4095;
  String frase = "Tensão do Potenciômetro: ";
  frase += voltagem;
  frase += " Valor do Sensor: ";
  frase += valorSensor;
  frase += " \nPorcentagem: ";
  frase += porcentagem;
  frase += "%";
  Serial.println(frase);
  delay(1000);
}
