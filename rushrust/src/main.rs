fn str_owner() -> String {
    let s1 = String::from("hello");
    let s2 = s1.clone();

    println!("s1 = {}, s2 = {}", s1, s2);
    return s2;
}

fn take_owner(s : String){
    println!("Take owner : {}", s);
}

fn take_back_owner(s : String) -> String {
    println!("Take owner : {}", s);
    s
}

fn pass_by_ref(s : &String) -> usize{
  s.len()
}

fn write_ref(s : &mut String){
  s.push_str("new world.");
}

//fn dangle() -> &String {
fn dangle() -> String {
  let s = String::from("hello");
  //&s // s already dead outside dangle()
  s
}

// use index instead of reference to part of var.
fn slice_first_word(s: &String) -> usize {
  let bytes = s.as_bytes();

  for (i, &item) in bytes.iter().enumerate() {
      if item == b' ' {
          return i;
      }
  }

  s.len()
}

fn slice_ref(s: &String) -> &str {
  let bytes = s.as_bytes();

  for (i, &item) in bytes.iter().enumerate() {
      if item == b' ' {
          return &s[0..i];
      }
  }

  &s[..]
}

fn main() {
    let mut s = str_owner();

    // Lost ownership of input var
    //take_owner(s);
    
    // Give back by return
    //s = take_back_owner(s);

    // Use ref instead to keep ownership
    let l = pass_by_ref(&s);

    // Mutable ref for editing
    let r = &mut s;
    r.push_str(" - ");
    write_ref(&mut s); // can not create 2nd mut ref before last usage or dead of 1st

    // slice
    let lw = slice_first_word(&s);
    let sw = slice_ref(&s);
    // s.clear() - clear will create mutable ref to truncate the string

    println!("Main : {} - 1st word = {} , {}",s,sw,lw);
}
