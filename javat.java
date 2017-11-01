class Main {
  public static void main(String[] args) {
    // 変数numbersに、与えられた数字の配列を代入してください
    int numbers[] = {1, 4, 6, 9, 13, 16};
    
    int oddSum = 0;
    int evenSum = 0;
    
    // for文を用いて、配列numbersの偶数の和と奇数の和を求めてください
    for (int i = 0; i < numbers.length; i++){
      if(i % 2 == 0){
        oddSum += numbers[i];
      }else{
        evenSum += numbers[i];
      }
    }

    System.out.println("奇数の和は" + oddSum + "です");
    System.out.println("偶数の和は" + evenSum + "です");
  }
}
