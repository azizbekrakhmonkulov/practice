
// TASK - F

// ❓ Shunday findDoublers function tuzing, unga faqat bitta string argument pass bolib,
// agar stringda bir hil harf qatnashgan bolsa true,
// qatnashmasa false qaytarishi kerak.

// ✅ Masalaning yechimi:
function findDoublers(str) {
    let counter = {};
    for (let harf of str) {
        if (counter[harf]) return true;
        counter[harf] = 1;
    }
    return false;
}

console.log(findDoublers("hello"));
console.log(findDoublers("world"));






// TASK - E

// ❓ Shunday function tuzing, u bitta string argumentni qabul qilib 
// osha stringni teskari qilib return qilsin.


// ✅ Masalaning yechimi:
// function getReverse(str) {
//     let result = "";
//     for (let i = str.length - 1; i >= 0; i--) {
//         result += str[i];
//     }
//     return result;
// }

// console.log(getReverse("NodeJS"));

// TASK - D

// ❓ Shunday function tuzingki unga integerlardan iborat array pass bolsin
// va function bizga osha arrayning eng katta qiymatiga tegishli 
// birinchi indexni qaytarsin.

// // ✅ Masalaning yechimi:
// function getArray(arr) {
//     let katta = arr[0]
//     let kattaIndex = 0;
//     for (let i = 0; i < arr.length; i++) {
//         if (arr[i] > katta) {
//             katta = arr[i]
//             kattaIndex = i
//         }
//     }

//     return kattaIndex
// }

// console.log(getArray([5, 11, 7, 24, 18]));



// TASK-C

// ❓ Shunday function tuzing, u 2ta string parametr ega bolsin,
//hamda agar har ikkala string bir hil harflardan iborat bolsa true
//aks holda false qaytarsin

// // ✅ Masalaning yechimi:
// function sameLetters(a, b) {
//     let sort1 = a.split("").sort().join("");
//     let sort2 = b.split("").sort().join("");


//     return sort1 === sort2;


// }
// result = sameLetters("night", "thing");
// console.log(result);


// TASK-B

// ❓ Shunday function tuzing, u 1ta string parametrga ega bolsin,
// hamda osha stringda
// qatnashgan raqamlarni sonini bizga return qilsin.

// ✅ Masalaning yechimi:

// function countNumbers(str) {
//     let count = 0;

//     for (let char of str) {
//         if (char >= '0' && char <= '9') {
//             count++;
//         }
//     }

//     return count;
// }

// let result = countNumbers("ajd212efdqfq");
// console.log("result:", result);


// /* TASK-A
// ❓ Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi
// parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
// */

// // ✅ Masalaning yechimi:
// function mevaHarfi(a, b) {
//     let soni = 0;

//     for (let harf of b) {
//         if (harf === a) {
//             soni++
//         }
//     }

//     return soni;
// }

// let result = mevaHarfi("o", "avocado");
// console.log(result)

