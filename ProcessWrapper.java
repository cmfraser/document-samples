/*
 * This class has been released under the MIT License:
 *
 * Copyright (c) 2020 Bioanalytical Computing, LLC
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

package com.bioanalyticalcomputing.util;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

/*
 * ProcessWrapper encapsulates the steps needed to run a program using the
 * ProcessBuilder class. To prevent side effects, ProcessWrapper decouples input
 * commands from its internal ProcessBuilder and uses wrapper methods to isolate
 * the state of the ProcessBuilder. ProcessWrapper removes direct access to all
 * ProcessBuilder methods and allows only indirect access to
 * ProcessBuilder.command() and ProcessBuilder.inheritIO().
 * ProcessWrapper.getCommand() returns a copy of the internal ProcessBuilder
 * command, and ProcessWrapper.setCommand() creates a copy of a new command for
 * the internal ProcessBuilder. ProcessWrapper sets the redirectErrorStream
 * property for the internal ProcessBuilder to true.
 *
 * Note that ProcessWrapper methods are not synchronized, and ProcessWrapper has
 * not been tested with external synchronization.
 *
 * Following are some simple ProcessWrapper examples (using Python 2.7.16 on
 * macOS Catalina):
 *
 *   // Run a program and print the output:
 *   ProcessWrapper processWrapper = new ProcessWrapper("python", "-c", "print('Hello, world!')");
 *   processWrapper.run();
 *   processWrapper.printOutput();
 *   // Expected output:
 *   // Hello, world!
 *
 *   // Modify the input:
 *   List<String> exampleCommand = processWrapper.getCommand();
 *   exampleCommand.remove(exampleCommand.size() - 1);
 *   exampleCommand.add("print('Hello')");
 *   processWrapper.setCommand(exampleCommand);
 *   processWrapper.run();
 *
 *   // Work with the output:
 *   List<String> exampleOutput = processWrapper.getOutput();
 *   if (exampleOutput.size() > 0)
 *     System.out.println(exampleOutput.get(0) + " again!");
 *   // Expected output:
 *   // Hello again!
 */
public final class ProcessWrapper {
    private ProcessBuilder processBuilder;
    private Process process;
    private BufferedReader bufferedReader;
    private ArrayList<String> output;

    /*
     * Passes the command to the second constructor.
     *
     * command - the command to be passed to the internal ProcessBuilder for
     *           execution
     */
    public ProcessWrapper(String... command) {
        this(Arrays.asList(command));
    }

    /*
     * Creates a ProcessWrapper and an internal ProcessBuilder using a copy of
     * the command. The internal command cannot be modified outside of
     * the constructed task builder (since the internal command List is a copy
     * and Strings are immutable).
     *
     * command - the command to be passed to the internal ProcessBuilder for
     *           execution
     */
    public ProcessWrapper(List<String> command) {
        processBuilder = new ProcessBuilder(new ArrayList<String>(command));
        processBuilder.redirectErrorStream(true);
        output = new ArrayList<String>();
    }

    /*
     * Calls the inheritIO() method of the internal ProcessBuilder.
     */
    public void inheritIO() {
        processBuilder.inheritIO();
    }

    /*
     * Returns a copy of the current ProcessBuilder command. Changes made to the
     * returned command will not be reflected in the state of the internal
     * ProcessBuilder (since the returned command List is a copy and Strings
     * are immutable).
     *
     * returns - a copy of the current ProcessBuilder command
     */
    public List<String> getCommand() {
        return new ArrayList<String>(processBuilder.command());
    }

    /*
     * Replaces the current command for the internal ProcessBuilder with a copy
     * of the passed command. Changes made to the original command will not be
     * reflected in the state of the internal ProcessBuilder (since the internal
     * command List is a copy and Strings are immutable).
     *
     * command - the new command to be copied into the internal ProcessBuilder
     */
    public void setCommand(List<String> command) {
        processBuilder.command(new ArrayList<String>(command));
        output.clear();
    }

    /*
     * Starts the internal ProcessBuilder and waits for completion of the
     * returned Process, catching any thrown exceptions.
     */
    private void executeProcess() {
        try {
            process = processBuilder.start();
            process.waitFor();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

    /*
     * Initializes the internal BufferedReader with the InputStream from the
     * internal Process.
     */
    private void initializeBufferedReader() {
        bufferedReader = new BufferedReader(
                new InputStreamReader(
                        process.getInputStream()));
    }

    /*
     * Returns a single line from the internal ProcessBuilder using the
     * readLine() method of the internal BufferedReader catching any thrown
     * exceptions.
     */
    private String readLine() {
        String myLine = null;
        try {
            myLine = bufferedReader.readLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
        return myLine;
    }

    /*
     * Extracts all lines from the internal ProcessBuilder and appends them to
     * the internal ProcessBuilder output.
     */
    private void extractOutput() {
        String myLine = null;
        while ((myLine = readLine()) != null)
            output.add(myLine);
    }

    /*
     * Executes the command specified by either a ProcessWrapper constructor or
     * ProcessWrapper.setCommand() and collects the output from the internal
     * ProcessBuilder.
     */
    public void run() {
        executeProcess();
        initializeBufferedReader();
        extractOutput();
    }

    /*
     * Returns a copy of the output from the command that the ProcessBuilder has
     * executed.
     *
     * returns - the output from the executed command
     */
    public List<String> getOutput() {
        return new ArrayList<String>(output);
    }

    /*
     * Prints the output from the command that the ProcessBuilder has executed.
     */
    public void printOutput() {
        for (int i = 0; i < output.size(); i++)
            System.out.println(output.get(i));
    }
}
