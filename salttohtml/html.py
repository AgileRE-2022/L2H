base = '''\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Salt to HTML Preview</title>

  <script src="https://unpkg.com/tailwindcss-jit-cdn">
  </script>
</head>

<body>
  <main class="flex w-screen h-screen">
    <div class="w-[calc(%dpx*14px)] m-auto p-6 border border-black border-opacity-10 rounded-lg">
      %s
    </div>
  </main>
</body>
</html>\
'''

plainText1 = '''
<p class="my-1 py-auto text-gray-700">
  %s
</p>\
'''

plainText2 = '''
<p class="my-1 py-auto font-medium">
  %s
</p>\
'''

button1 = '''
<a href="#">
<button class="w-[calc(%dpx*14)] my-1 py-2 font-medium tracking-wide text-white capitalize transition-colors duration-200 transform bg-blue-600 rounded-md hover:bg-blue-500 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-80">
  <a href="">
    %s
  </a>
</button>
</a>\
'''

button2 = '''
<a href="#"><button
  type="submit"
  class="w-[calc(%dpx*14)] my-1 items-center justify-center h-10 font-medium tracking-wide text-white transition duration-200 rounded-full shadow-md bg-yellow-500 hover:bg-yellow-600 focus:shadow-outline focus:outline-none"
>
  %s
</button></a>\
'''

uncheckedRadio1 = '''
<div class="form-check">
  <input
    class="form-check-input rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain float-left mr-2 cursor-pointer"
    type="radio"
    name="radio%d"
    id="%s"
  />
  <label
    class="form-check-label inline-block text-gray-700" 
    for="%s"
  >
    %s
  </label>
</div>\
'''

uncheckedRadio2 = '''
<div class="form-check">
  <input
    class="form-check-input w-4 h-4 text-yellow-500 bg-gray-100 rounded-full border-gray-300 focus:ring-yellow-500 dark:focus:ring-yellow-500 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
    type="radio"
    name="radio%d"
    id="%s"
  />
  <label
    class="form-check-label inline-block text-gray-700" 
    for="%s"
  >
    %s
  </label>
</div>\
'''

checkedRadio1 = '''
<div class="form-check">
  <input
    checked
    class="form-check-input rounded-full h-4 w-4 border border-gray-300 bg-white checked:bg-blue-600 checked:border-blue-600 focus:outline-none transition duration-200 mt-1 align-top bg-no-repeat bg-center bg-contain float-left mr-2 cursor-pointer"
    type="radio"
    name="radio%d"
    id="%s"
  />
  <label
    class="form-check-label inline-block text-gray-700" 
    for="%s"
  >
    %s
  </label>
</div>\
'''

checkedRadio2 = '''
<div class="form-check">
  <input
    checked
    class="form-check-input w-4 h-4 text-yellow-500 bg-gray-100 rounded-full border-gray-300 focus:ring-yellow-500 dark:focus:ring-yellow-500 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
    type="radio"
    name="radio%d"
    id="%s"
  />
  <label
    class="form-check-label inline-block text-gray-700" 
    for="%s"
  >
    %s
  </label>
</div>\
'''

uncheckedBox1 = '''
<div class="form-check">
  <input
    class="w-4 h-4 text-blue-600 bg-gray-100 rounded border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
    type="checkbox"
    name="uncheckedBox1"
    id="%s"
  />
  <label
    class="form-check-label inline-block text-gray-800" 
    for="%s"
  >
    %s
  </label>
</div>\
'''

uncheckedBox2 = '''
<div class="form-check">
  <input
    class="w-4 h-4 text-yellow-500 bg-gray-100 rounded border-gray-300 focus:ring-yellow-500 dark:focus:ring-yellow-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
    type="checkbox"
    name="uncheckedBox2"
    id="%s"
  />
  <label
    class="form-check-label inline-block text-gray-800" 
    for="%s"
  >
    %s
  </label>
</div>\
'''

checkedBox1 = '''
<div class="form-check">
  <input
    checked
    class="w-4 h-4 text-blue-600 bg-gray-100 rounded border-gray-300 focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
    type="checkbox"
    name="checkedBox1"
    id="%s"
  />
  <label
    class="form-check-label inline-block text-gray-800" 
    for="%s"
  >
    %s
  </label>
</div>\
'''

checkedBox2 = '''
<div class="form-check">
  <input
    checked
    class="w-4 h-4 text-yellow-500 bg-gray-100 rounded border-gray-300 focus:ring-yellow-500 dark:focus:ring-yellow-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
    type="checkbox"
    name="checkedBox2"
    id="%s"
  />
  <label
    class="form-check-label inline-block text-gray-800" 
    for="%s"
  >
    %s
  </label>
</div>\
'''

inputText1 = '''
<form>
  <input
    id="%s"
    type="text"
    class="w-[calc(%dpx*0+100)] truncate my-1 py-2 text-gray-700 bg-white border rounded-md focus:border-blue-400 focus:outline-none focus:ring focus:ring-blue-300 focus:ring-opacity-40"
    placeholder="%s"
  >
</form>\
'''

inputText2 = '''
<form>
  <input
    id="%s"
    type="text"
    class="w-[calc(%dpx*0+100)] truncate h-10 my-1 transition duration-200 bg-white border border-gray-300 rounded-full shadow-sm appearance-none focus:border-yellow-400 focus:outline-none focus:shadow-outline focus:ring-yellow-500"
    placeholder="%s"
    name="name"
  >
</form>\
'''

dropList1 = '''
<button
  class="relative z-10 flex items-center p-2 text-gray-600 bg-white border border-transparent rounded-md focus:border-blue-500 focus:ring-opacity-40 focus:ring-blue-300 focus:ring focus:outline-none"
>
  <span class="pl-[2px] pr-[calc(%dpx*4-2px)]">
    %s
  </span>
  <svg
    class="w-5 h-5 mx-1"
    viewBox="0 0 24 24"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <path d="M12 15.713L18.01 9.70299L16.597 8.28799L12 12.888L7.40399 8.28799L5.98999 9.70199L12 15.713Z" fill="currentColor">
    </path>
  </svg>
</button>\
'''

dropList2 = '''
<button
  type="button"
  class="border border-gray-300 bg-white dark:bg-gray-800 shadow-sm flex items-center justify-center rounded-full px-4 py-2 font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-100 focus:ring-gray-500"
  id="options-menu"
>
  <span class="pl-[2px] pr-[calc(%dpx*4-14px)]">
    %s
  </span>
  <svg
    width="20"
    height="20"
    fill="currentColor"
    viewBox="0 0 1792 1792"
    xmlns="http://www.w3.org/2000/svg"
  >
      <path d="M1408 704q0 26-19 45l-448 448q-19 19-45 19t-45-19l-448-448q-19-19-19-45t19-45 45-19h896q26 0 45 19t19 45z">
      </path>
  </svg>
</button>\
'''

divOpen  = "<div>"

divClose = "\n</div>"

newLine = "\n<br>\n<br>"

div = '''\
<div>
%s
</div>
'''

gridView1 = '''\
    <div class="grid grid-cols-%d auto-cols-max gap-4 flex justify-center items-center">
        %s
    </div>
'''
gridView2 = '''\
    <div class="grid grid-cols-%d auto-cols-max gap-4 flex justify-center items-center">
        %s
    </div>
'''