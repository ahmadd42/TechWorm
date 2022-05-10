//a simple program to demonstrate the use of stream in java
import java.util.*;
import java.util.stream.*;

class StreamDemo2 {

public static void main (String args[]) {

List<Integer> numbers = Arrays.asList(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20);
List<Integer> score = Arrays.asList(55,66,22,89,13,114,250,10,5,25,3,16,78);
List<String> names = Arrays.asList("Ahmad","Ashar","Riffat","Memoona","Arooj","Mustansar");

//Find even numbers in the numbers list and store it in a separate list
List<Integer> even = numbers.stream().filter(n->n%2==0).collect(Collectors.toList());
System.out.println("Even numbers in the list :");
//for (Integer ev:even)     One way of displaying list values
//System.out.println(ev);
even.forEach(System.out::println); //Other way of diaplaying list values

int num = score.stream().reduce(0,(a,b)->(a>b)?a:b); //Find max method 1
//int num = score.stream().reduce(0,(a,b)->Integer.max(a,b)); //Find max method 2
//int num = Collections.max(score,null); //Find max method 3
System.out.println("Maximum value : " + num);

Optional<String> longest = names.stream().reduce((n1,n2)->(n1.length()>n2.length())?n1:n2);
if(longest.isPresent())
System.out.println("Longest name : " + longest.get());
else
System.out.println("Not found");
}
}
