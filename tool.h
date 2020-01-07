


/*********************************************************************
 *
 * Function    :  hash_string
 *
 * Description :  Take a string and compute a (hopefuly) unique numeric
 *                integer value. This is useful to "switch" a string.
 *
 * Parameters  :
 *          1  :  s : string to be hashed.
 *
 * Returns     :  The string's hash
 *
 *********************************************************************/
unsigned int hash_string(const char* s)
{
   unsigned int h = 0;

   for (; *s; ++s)
   {
      h = 5 * h + (unsigned int)*s;
   }

   return (h);

}