module Main where
import System.Environment

main :: IO ()
main = do args <- getArgs
          putStrLn("Hello, Haskel!!" ++ args !! 0  ++ "arg2: " ++ args !! 1)
